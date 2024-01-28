"""Test cases for custom builders."""
import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("fts-index", testroot="default")
def test___work_builder(app: SphinxTestApp, status, warning, conn):  # noqa
    app.build()
    assert len(conn.execute("SELECT * FROM document").fetchall()) > 0
    assert len(conn.execute("SELECT * FROM section").fetchall()) > 0
    assert len(conn.execute("SELECT * FROM content").fetchall()) > 0
