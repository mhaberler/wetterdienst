###########################################
Wetterdienst - Open weather data for humans
###########################################


Introduction
************
Welcome to Wetterdienst, your friendly weather service library for Python.

We are a group of like-minded people trying to make access to weather data in
Python feel like a warm summer breeze, similar to other projects like
rdwd_ for the R language, which originally drew our interest in this project.

While our long-term goal is to provide access to multiple weather services,
we are still stuck with the German Weather Service (DWD). Contributions are
always welcome!

This program and its repository tries to use modern Python technologies
all over the place. The library is based on Pandas across the board,
uses Poetry for package administration and GitHub actions for
all things CI.


Features
********

Coverage
========
The library currently covers

- historical weather data from ground stations
- RADOLAN fitted radar data for areal precipitation
- MOSMIX statistical optimized scalar forecasts extracted from weather models

To get better insight on which data we have currently made available, with this library
take a look at `data coverage`_.


Details
=======
- Get metadata for a set of Parameter, PeriodType and TimeResolution.
- Get station(s) nearby a selected location for a given set.
- Store/recover collected data.
- Docker image to run the library dockerized.
- Client to run the library from command line.


Setup
*****
Run the following to make ``wetterdienst`` available in your current environment:

.. code-block:: bash

    pip install wetterdienst

Synopsis
********
Get historical data for specific stations, using Python:

.. code-block:: python

    from wetterdienst.dwd.observations import DWDObservationData, DWDObsParameterSet,
        DWDObsPeriodType, DWDObsTimeResolution

    observations = DWDObservationData(
        station_ids=[1048,4411],
        parameter=[DWDObsParameterSet.CLIMATE_SUMMARY, DWDObsParameterSet.SOLAR],
        time_resolution=DWDObsTimeResolution.DAILY,
        start_date="1990-01-01",
        end_date="2020-01-01",
        tidy_data=True,
        humanize_column_names=True,
    )

    for df in observations.collect_data():
        # analyse the station here

Get data for specific stations from the command line:

.. code-block:: bash

    # Get list of all stations for daily climate summary data in JSON format
    wetterdienst stations --parameter=kl --resolution=daily --period=recent

    # Get daily climate summary data for specific stations
    wetterdienst readings --station=1048,4411 --parameter=kl --resolution=daily --period=recent


Documentation
*************
We strongly recommend reading the full documentation, which will be updated continuously
as we make progress with this library:

    - https://wetterdienst.readthedocs.io/

For the whole functionality, check out the `Wetterdienst API`_ section of our
documentation, which will be constantly updated. To stay up to date with the
development, take a look at the changelog_. Also, don't miss out our examples_.


Data license
************
Although the data is specified as being open, the DWD asks you to reference them as
copyright owner. Please take a look at the `Open Data Strategy at the DWD`_ and the
`Official Copyright`_ statements before using the data.


.. _rdwd: https://github.com/brry/rdwd
.. _Wetterdienst API: https://wetterdienst.readthedocs.io/en/latest/pages/api.html
.. _data coverage: https://wetterdienst.readthedocs.io/en/latest/pages/data_coverage.html
.. _changelog: https://wetterdienst.readthedocs.io/en/latest/pages/api.html
.. _examples: https://github.com/earthobservations/wetterdienst/tree/master/example
.. _Open Data Strategy at the DWD: https://www.dwd.de/EN/ourservices/opendata/opendata.html
.. _Official Copyright: https://www.dwd.de/EN/service/copyright/copyright_artikel.html?nn=495490&lsbId=627548
