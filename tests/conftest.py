"""Configuration for pytest."""
import os

import pytest
from sphinx.testing.path import path

from tests.util import Database

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


@pytest.fixture(scope="session")
def database_dsn():
    """Pytest fixture providing the database connection string for software tests."""
    return "postgresql://postgres@localhost:5432"


@pytest.fixture(scope="session")
def database(database_dsn):
    """Pytest fixture returning a database wrapper object."""
    return Database(database_dsn)


@pytest.fixture
def conn(database):
    """
    Pytest fixture returning a database wrapper object, with content cleared.

    This is intended to provide each test case with a blank slate.
    """
    if "POSTGRES_LOG_STATEMENT" in os.environ:
        database.execute(f"SET log_statement='{os.environ['POSTGRES_LOG_STATEMENT']}';")
    database.reset()
    return database


@pytest.fixture(scope="session")
def rootdir():
    """Set root directory to use testing sphinx project."""
    return path(__file__).parent.abspath() / "roots"
