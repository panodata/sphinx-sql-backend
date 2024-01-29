# noqa: D100
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import atsphinx.sqlite3fts

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "atsphinx-sqlite3fts"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = atsphinx.sqlite3fts.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ["sphinx.ext.githubpages", "sphinx.ext.intersphinx", "atsphinx.sqlite3fts"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_title = f"{project} v{release}"
html_theme = "furo"
html_static_path = ["_static"]

# -- Options for extensions
# sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# atsphinx-sqlite3fts
sqlite3fts_use_search_html = True
sqlite3fts_database_url = "postgresql://postgres@localhost:5432"


def setup(app):  # noqa: D103
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
