#####
Setup
#####

Wetterdienst can be used by either installing it on
your workstation or within a Docker container.


******
Native
******
The installation of ``wetterdienst`` can happen via PyPI or directly from GitHub. The GitHub
version will always include most recent changes that may not have been released to PyPI.

PyPI

.. code-block:: bash

    pip install wetterdienst

GitHub

.. code-block:: bash

    pip install git+https://github.com/earthobservations/wetterdienst

There are some extras available for ``wetterdienst``. Use them like::

    pip install wetterdienst[http,sql]

- docs: Install the Sphinx documentation generator.
- ipython: Install iPython stack.
- excel: Install openpyxl for Excel export.
- http: Install HTTP API prerequisites.
- sql: Install DuckDB for querying data using SQL.
- duckdb: Install support for DuckDB.
- influxdb: Install support for InfluxDB.
- cratedb: Install support for CrateDB.
- mysql: Install support for MySQL.
- postgresql: Install support for PostgreSQL.

In order to check the installation, invoke::

    wetterdienst --help



.. _run-in-docker:

******
Docker
******
Docker images for each stable release will get pushed to GitHub Container Registry.

There are images in two variants, ``wetterdienst-standard`` and ``wetterdienst-full``.

``wetterdienst-standard`` will contain a minimum set of 3rd-party packages,
while ``wetterdienst-full`` will try to serve a full environment by also
including packages like GDAL and wradlib.

Library
=======
Use the latest stable version of Wetterdienst::

    $ docker run -ti ghcr.io/earthobservations/wetterdienst-standard
    Python 3.8.5 (default, Sep 10 2020, 16:58:22)
    [GCC 8.3.0] on linux

    >>> import wetterdienst
    >>> wetterdienst.__version__
    '0.7.0'

Command line script
===================
The ``wetterdienst`` command is also available::

    # Make an alias to use it conveniently from your shell.
    alias wetterdienst='docker run -ti ghcr.io/earthobservations/wetterdienst-standard wetterdienst'

    wetterdienst --version
    wetterdienst --help
