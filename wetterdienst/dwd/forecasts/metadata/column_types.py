from wetterdienst.dwd.forecasts.metadata.parameter import DWDMosmixParameter
from wetterdienst.dwd.metadata.column_names import DWDMetaColumns

DATE_FIELDS_REGULAR = DWDMetaColumns.DATETIME.value

INTEGER_PARAMETERS = (
    DWDMosmixParameter.WIND_DIRECTION.value,
    DWDMosmixParameter.WEATHER_LAST_6H.value,
    DWDMosmixParameter.WEATHER_SIGNIFICANT_OPTIONAL_LAST_1H,
    DWDMosmixParameter.WEATHER_SIGNIFICANT_OPTIONAL_LAST_3H,
    DWDMosmixParameter.WEATHER_SIGNIFICANT_OPTIONAL_LAST_6H,
    DWDMosmixParameter.WEATHER_SIGNIFICANT_OPTIONAL_LAST_12H,
    DWDMosmixParameter.WEATHER_SIGNIFICANT_OPTIONAL_LAST_24H,
    DWDMosmixParameter.WEATHER_SIGNIFICANT.value,
    DWDMosmixParameter.WEATHER_SIGNIFICANT_LAST_3H.value,
    DWDMosmixParameter.PROBABILITY_WIND_GUST_GE_25_KN_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_WIND_GUST_GE_40_KN_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_WIND_GUST_GE_55_KN_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_FOG_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_FOG_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_FOG_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_0_MM_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_2_MM_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_2_MM_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_2_MM_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_1_0_MM_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_5_0_MM_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_5_0_MM_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_5_0_MM_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_DRIZZLE_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_STRAT_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_CONV_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_THUNDERSTORM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_LIQUID_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_SOLID_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_FREEZING_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_VISIBILITY_BELOW_1000_M.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_0_MM_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_1_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_2_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_3_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_5_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_7_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_1_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_2_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_0_PCT_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_30_PCT_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_60_PCT_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_RADIATION_GLOBAL_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_3_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_5_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_10_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_10_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_15_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_25_0_MM_LAST_1H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_STRAT_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_CONV_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_THUNDERSTORM_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_LIQUID_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_FREEZING_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_SOLID_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_DRIZZLE_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_FOG_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_WIND_GUST_GE_25_KN_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_WIND_GUST_GE_40_KN_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_WIND_GUST_GE_55_KN_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_STRAT_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_CONV_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_THUNDERSTORM_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_LIQUID_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_FREEZING_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_SOLID_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_DRIZZLE_LAST_12H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_1_0_MM_LAST_6H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_0_0_MM_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_GT_1_0_MM_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_PRECIPITATION_LAST_24H.value,
    DWDMosmixParameter.PROBABILITY_THUNDERSTORM_LAST_24H.value,
)
