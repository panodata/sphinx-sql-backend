"""Configuration is cases for default behavior."""
extensions = [
    "atsphinx.sqlite3fts",
]

sqlite3fts_database_url = "postgresql://postgres@localhost:5432"

# To skip toctree
rst_prolog = """
:orphan:
"""
