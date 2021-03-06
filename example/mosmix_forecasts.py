"""
=====
About
=====
Example for DWD MOSMIX acquisition.

This program will request latest MOSMIX-L data for
stations 01001 and 01008 and parameters DD and ww.

Other MOSMIX variants are also listed and can be
enabled on demand.
"""
from wetterdienst.dwd.forecasts.metadata.dates import DWDForecastDate
from wetterdienst.dwd.forecasts import DWDMosmixData, DWDMosmixType
from wetterdienst.util.cli import setup_logging


def mosmix_example():

    # A. MOSMIX-L -- Specific stations - each station with own file
    mosmix = DWDMosmixData(
        station_ids=["01001", "01008"],
        parameters=["DD", "ww"],
        start_issue=DWDForecastDate.LATEST,  # automatically set if left empty
        mosmix_type=DWDMosmixType.LARGE,
        tidy_data=True,
        humanize_parameters=True,
    )
    response = next(mosmix.query())

    # meta data enriched with information from metadata_for_forecasts()
    output_section("Metadata", response.metadata)
    output_section("Forecasts", response.data)

    # B. MOSMIX-S -- All stations - specified stations are extracted.
    mosmix = DWDMosmixData(
        station_ids=["01028", "01092"],
        parameters=["DD", "ww"],
        start_issue=DWDForecastDate.LATEST,  # automatically set if left empty
        mosmix_type=DWDMosmixType.SMALL,
        tidy_data=True,
        humanize_parameters=True,
    )
    response = next(mosmix.query())

    output_section("Metadata", response.metadata)
    output_section("Forecasts", response.data)


def output_section(title, data):  # pragma: no cover
    print("-" * len(title))
    print(title)
    print("-" * len(title))
    print(data)
    print()


def main():
    setup_logging()
    mosmix_example()


if __name__ == "__main__":
    main()
