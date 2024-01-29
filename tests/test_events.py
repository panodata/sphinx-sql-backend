"""Test cases for result of events."""
import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="default")
def test___work_builder(app: SphinxTestApp, status, warning, conn):  # noqa
    app.build()
    assert len(conn.execute("SELECT * FROM document").fetchall()) > 0
