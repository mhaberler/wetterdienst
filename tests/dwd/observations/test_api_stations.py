import pytest
from pandas import Timestamp

from wetterdienst.dwd.metadata.column_names import DWDMetaColumns
from wetterdienst.dwd.observations import (
    DWDObservationParameterSet,
    DWDObservationPeriod,
    DWDObservationResolution,
)
from wetterdienst.dwd.observations.api import DWDObservationStations
from wetterdienst.exceptions import InvalidParameterCombination


@pytest.mark.remote
def test_dwd_observation_sites_success():

    # Existing combination of parameters
    sites = DWDObservationStations(
        DWDObservationParameterSet.CLIMATE_SUMMARY,
        DWDObservationResolution.DAILY,
        DWDObservationPeriod.HISTORICAL,
    ).all()

    assert not sites.empty

    assert sites.loc[
        sites[DWDMetaColumns.STATION_ID.value] == "00001", :
    ].values.tolist() == [
        [
            "00001",
            Timestamp("19370101").tz_localize("UTC"),
            Timestamp("19860630").tz_localize("UTC"),
            478.0,
            47.8413,
            8.8493,
            "Aach",
            "Baden-Württemberg",
        ]
    ]


def test_dwd_observation_sites_fail():
    with pytest.raises(InvalidParameterCombination):
        DWDObservationStations(
            DWDObservationParameterSet.CLIMATE_SUMMARY,
            DWDObservationResolution.MINUTE_1,
            DWDObservationPeriod.HISTORICAL,
        ).all()


@pytest.mark.remote
def test_dwd_observation_sites_geojson():

    # Existing combination of parameters
    df = DWDObservationStations(
        DWDObservationParameterSet.CLIMATE_SUMMARY,
        DWDObservationResolution.DAILY,
        DWDObservationPeriod.HISTORICAL,
    ).all()

    assert not df.empty

    df = df[df[DWDMetaColumns.STATION_ID.value] == "00001"]

    geojson = df.dwd.to_geojson()

    properties = geojson["features"][0]["properties"]
    geometry = geojson["features"][0]["geometry"]

    assert properties["name"] == "Aach"
    assert properties["state"] == "Baden-Württemberg"

    assert geometry == {
        "type": "Point",
        "coordinates": [8.8493, 47.8413, 478.0],
    }
