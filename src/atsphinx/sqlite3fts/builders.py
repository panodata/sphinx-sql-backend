"""Management custom builders."""
from typing import Set

from sphinx.builders import Builder
from sphinx.util.docutils import nodes

from . import models, services


class FtsIndexer(Builder):
    """
    Fulltext index builder for databases.

    A custom builder to generate fulltext indexes, stored in SQL databases.
    """

    name = "fts-index"
    allow_parallel = True

    def get_target_uri(self, docname: str, typ: str = None) -> str:  # noqa: D102
        return docname

    def get_outdated_docs(self) -> str:  # noqa: D102
        return "db.sqlite"

    def prepare_writing(self, docnames: Set[str]) -> None:  # noqa: D102
        from atsphinx.sqlite3fts.models import Content, Document, Section

        Document.truncate_table(cascade=True)
        Section.truncate_table(cascade=True)
        Content.truncate_table(cascade=True)

    def write_doc(self, docname: str, doctree: nodes.document) -> None:
        """Register content of document into database.

        This method only insert into db, does not write file.
        """
        if docname in self.config.sqlite3fts_exclude_pages:
            return
        document, sections = services.parse_document(doctree, docname)
        models.store_document(document, sections)
