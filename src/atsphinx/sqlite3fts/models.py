"""
Database schema / ORM entity definition.

- atsphinx-sqlite3fts is using SQLite.
- sphinx-sql-backend is aiming to add support for others.

TODO: Add support for multiple database backends?
"""
import os
from pathlib import Path
from typing import Iterable

from peewee import SQL, fn
from playhouse import postgres_ext as ext

from atsphinx.sqlite3fts.playhouse import TSVectorFieldPlus

db_proxy = ext.DatabaseProxy()


class Document(ext.Model):
    """Document main model."""

    page = ext.TextField(null=False, unique=True)
    title = ext.TextField(null=False)

    class Meta:  # noqa: D106
        database = db_proxy


class Section(ext.Model):
    """Section unit of document."""

    document = ext.ForeignKeyField(Document)
    root = ext.BooleanField(default=False, null=False)
    ref = ext.TextField(null=False)
    title = ext.TextField(null=False)
    body = ext.TextField(null=False)

    class Meta:  # noqa: D106
        database = db_proxy


class Content(ext.Model):
    """Searching model."""

    rowid = ext.IntegerField()
    title = TSVectorFieldPlus()
    body = TSVectorFieldPlus()

    class Meta:  # noqa: D106
        database = db_proxy
        # TODO: This is an option from SQLite, it does not work on other DBMS.
        # options = {"tokenize": "trigram"}


def store_document(document: Document, sections: Iterable[Section]):
    """Save document data into database."""
    document.save()
    for section in sections:
        section.document = document
        section.save()
        Content.insert(
            {
                Content.rowid: section.id,
                Content.title: fn.to_tsvector(section.title or document.title),
                Content.body: fn.to_tsvector(section.body),
            }
        ).execute()


def search_documents(keyword: str) -> Iterable[Section]:
    """Search documents from keyword by full-text-search."""
    # SQLite.
    """
    return (
        Section.select()
        .join(Content, on=(Section.id == Content.rowid))
        .where(Content.match(keyword))
        .order_by(Content.bm25())
    )
    """

    # PostgreSQL.
    # https://www.postgresql.org/docs/current/textsearch-controls.html
    # https://stackoverflow.com/questions/25033184/postgresql-full-text-search-performance-not-acceptable-when-ordering-by-ts-rank/25245291#25245291
    return (
        Section.select(
            Section,
            fn.ts_rank_cd(Content.title, fn.websearch_to_tsquery(keyword), 32).alias(
                "rank_title"
            ),
            fn.ts_rank_cd(Content.body, fn.websearch_to_tsquery(keyword), 32).alias(
                "rank_body"
            ),
        )
        .join(Content, on=(Section.id == Content.rowid))
        .where(
            Content.title.match(keyword, web=True)
            | Content.body.match(keyword, web=True)
        )
        .order_by(
            SQL("rank_title").desc(),
            SQL("rank_body").desc(),
        )
    )


def bind(db_type: str, db_path: Path):
    """Bind connection.

    This works only set db into proxy, not included creating tables.
    """
    if db_type == "sqlite":
        db = ext.SqliteExtDatabase(db_path)
    elif db_type == "postgresql":
        db = ext.PostgresqlExtDatabase(db_path)
        if "POSTGRES_LOG_STATEMENT" in os.environ:
            db.execute_sql(
                f"SET log_statement='{os.environ['POSTGRES_LOG_STATEMENT']}';"
            )
    else:
        raise ValueError(f"Unknown database type: {db_type}")
    db_proxy.initialize(db)


def initialize(db_type: str, db_path: Path):
    """Bind connection and create tables."""
    bind(db_type, db_path)
    db_proxy.create_tables([Document, Section, Content])
