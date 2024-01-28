"""Test cases for model."""
import pytest
from sphinx.testing.util import SphinxTestApp

from atsphinx.sqlite3fts import models


@pytest.mark.sphinx("fts-index", testroot="default")
def test_search_one_hit(app: SphinxTestApp, status, warning, conn):
    """Verify searching with one hit."""
    app.build()
    sections = list(models.search_documents("Sub 1-2"))
    assert len(sections) == 1

    assert sections[0].document.page == "index"
    assert sections[0].document.title == "Test document"
    assert sections[0].ref == "section-1"
    assert sections[0].title == "Section 1"
    assert sections[0].body == "Sub 1-1\n\nFirst content\nSub 1-2\n\nSecond content"


@pytest.mark.sphinx("fts-index", testroot="default")
def test_search_two_hits(app: SphinxTestApp, status, warning, conn):
    """Verify searching with two hits."""
    app.build()
    sections = list(models.search_documents("section"))
    assert len(sections) == 2

    assert sections[0].document.page == "index"
    assert sections[0].document.title == "Test document"
    assert sections[0].ref == "section-1"
    assert sections[0].title == "Section 1"
    assert sections[0].body == "Sub 1-1\n\nFirst content\nSub 1-2\n\nSecond content"

    assert sections[1].document.page == "index"
    assert sections[1].document.title == "Test document"
    assert sections[1].ref == "section-2"
    assert sections[1].title == "Section 2"
    assert sections[1].body == "Sub 2-1\n\nEnd"
