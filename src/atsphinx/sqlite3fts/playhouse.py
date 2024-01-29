"""Peewee/Playhouse extension."""
from peewee import Expression, Field, TextField, fn
from playhouse.postgres_ext import TS_MATCH, IndexedFieldMixin


class TSVectorFieldPlus(IndexedFieldMixin, TextField):
    """An advanced `TSVectorField`, capable to use `websearch_to_tsquery`."""

    field_type = "TSVECTOR"
    __hash__ = Field.__hash__

    def match(self, query, language=None, plain=False, web=False):
        """Run match."""
        params = (language, query) if language is not None else (query,)
        func = fn.plainto_tsquery if plain else fn.to_tsquery
        if web:
            func = fn.websearch_to_tsquery
        return Expression(self, TS_MATCH, func(*params))
