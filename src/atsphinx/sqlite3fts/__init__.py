"""Sphinx document searcher using SQL database."""
from sphinx.application import Sphinx

from . import builders, events

__version__ = "0.1.3"


def setup(app: Sphinx):
    """Entrypoint as Sphinx extension."""
    app.add_config_value("sqlite3fts_exclude_pages", [], "env")
    app.add_config_value("sqlite3fts_use_search_html", False, "env")
    app.add_config_value("sqlite3fts_database_url", None, "env")
    app.add_builder(builders.FtsIndexer)
    app.connect("config-inited", events.setup_search_html)
    app.connect("config-inited", events.configure_database)
    app.connect("html-page-context", events.register_document)
    app.connect("build-finished", events.save_database)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
    }
