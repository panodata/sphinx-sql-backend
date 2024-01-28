==================
sphinx-sql-backend
==================

SQL backend for the Sphinx documentation generator.

.. image:: https://img.shields.io/pypi/v/sphinx-sql-backend.svg
    :target: https://pypi.org/project/sphinx-sql-backend/

.. image:: https://github.com/panodata/sphinx-sql-backend/actions/workflows/main.yml/badge.svg?branch=main
   :alt: Run CI
   :target: https://github.com/panodata/sphinx-sql-backend/actions/workflows/main.yml

.. image:: https://readthedocs.org/projects/sphinx-sql-backend/badge/?version=latest
    :target: https://sphinx-sql-backend.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

What's inside
=============

A Sphinx extension to provide Full-Text-Search (FTS) based on SQL
databases.

The package is completely based on `atsphinx-sqlite3fts`_ by
`Kazuya Takei`_, so many kudos and thanks go out to him.
See also `sqlite3fts on GitHub`_.

Status
======

Please note that the ``sphinx-sql-backend`` package contains alpha-, beta- and
incubation-quality code, and as such, is considered to be a work in progress.
Contributions of all kinds are much welcome, in order to make it more solid,
and to add features.

Breaking changes should be expected until a 1.0 release, so version pinning is
strongly recommended, especially when you use it as a library.

How it works
============

* Indexing: When running ``sphinx-build``, store documents into database.
* Searching: Provide backend service for responding to search requests and
  search-as-you-type UI based on `readthedocs-sphinx-search`_.

Installation
============

.. code-block:: console

   pip install git+https://github.com/panodata/sphinx-sql-backend.git

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

   python -m http.server -d _build/html

  Please access http://localhost:8000/search.html


Development
===========

Install package in development mode::

    pip install --editable='.[cli,docs,test]' --prefer-binary

Start PostgreSQL server::

    docker run --rm -it --publish=5432:5432 --env "POSTGRES_HOST_AUTH_METHOD=trust" postgres:16 postgres -c log_statement=all

Invoke software tests::

    export POSTGRES_LOG_STATEMENT=all
    pytest -vvv

Invoke linters::

    pip install pre-commit
    pre-commit run --all-files


.. _atsphinx-sqlite3fts: https://pypi.org/project/atsphinx-sqlite3fts/
.. _Kazuya Takei: https://github.com/attakei
.. _readthedocs-sphinx-search: https://github.com/readthedocs/readthedocs-sphinx-search
.. _sqlite3fts on GitHub: https://github.com/atsphinx/sqlite3fts
