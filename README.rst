===================
atsphinx-sqlite3fts
===================

Power search for Sphinx by SQLite3-FTS extension.

.. image:: https://img.shields.io/pypi/v/atsphinx-sqlite3fts.svg
    :target: https://pypi.org/project/atsphinx-sqlite3fts/

.. image:: https://github.com/atsphinx/sqlite3fts/actions/workflows/main.yml/badge.svg?branch=main
   :alt: Run CI
   :target: https://github.com/atsphinx/sqlite3fts/actions/workflows/main.yml

.. image:: https://readthedocs.org/projects/atsphinx-sqlite3fts/badge/?version=latest
    :target: https://atsphinx-sqlite3fts.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. note:: This is experimental library

Overview
========

This is sphinx extension to provide search component with full-text search database.

When ``sphinx-build`` runs with this extension, builder generate these components.

* SQLite database with FTS extension
* Records of all documents
* Search page HTML with sql.js

This will be useful when you want to embed strong full-text search with keeping static-site structure.

Installation
============

.. code-block:: console

   pip install atsphinx-sqlite3fts

Usage
=====

1. Register extension into your ``conf.py`` and configure it.

.. code-block:: python

   extensions = [
       #
       # Other extensions
       #
       "atsphinx.sqlite3fts",  # Add it
   ]

2. Run builder (html-based builder only).

.. code-block:: console

   sphinx-build -M html source build

3. To try it in local, use ``http.server`` module.

.. code-block:: console

   python -m http.server -d build

  Please access http://localhost:8000/search.html
