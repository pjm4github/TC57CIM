# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# No imports as they are not applicable to enums in Python
from enum import StrEnum


class WeatherCodeKind(StrEnum):
    """
    Kinds of weather conditions.
    @author tviegut
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    HAIL = 'A'  # weather code ("Hail")
    BLOWING_DUST = 'BD'  # weather code ("Blowing Dust")
    BLOWING_SAND = 'BN'  # weather code ("Blowing Sand")
    MIST = 'BR'  # weather code ("Mist")
    BLOWING_SNOW = 'BS'  # weather code ("Blowing Snow")
    FOG = 'F'  # weather code ("Fog")
    FROST = 'FR'  # weather code ("Frost")
    HAZE = 'H'  # weather code ("Haze")
    ICE_CRYSTALS = 'IC'  # weather code ("Ice Crystals")
    ICE_FOG = 'IF'  # weather code ("Ice Fog")
    SLEET = 'IP'  # weather code ("Ice Pellets/Sleet")
    SMOKE = 'K'  # weather code ("Smoke")
    DRIZZLE = 'L'  # weather code ("Drizzle")
    RAIN = 'R'  # weather code ("Rain")
    RAIN_SHOWERS = 'RW'  # weather code ("Rain Showers")
    RAIN_SNOW_MIX = 'RS'  # weather code ("Rain/Snow Mix")
    SNOW_SLEET_MIX = 'SI'  # weather code ("Snow/Sleet Mix")
    WINTRY_MIX = 'WS'  # weather code ("Wintry Mix")
    SNOW = 'S'  # weather code ("Snow")
    SNOW_SHOWERS = 'SW'  # weather code ("Snow Showers")
    THUNDER_STORMS = 'T'  # weather code ("Thunder Storms")
    VOLCANIC_ASH = 'VA'  # weather code ("Volcanic Ash")
    WATER_SPOUTS = 'WP'  # weather code ("Water Spouts")
    FREEZING_SPRAY = 'ZF'  # weather code ("Freezing Spray")
    FREEZING_DRIZZLE = 'ZL'  # weather code ("Freezing Drizzle")
    FREEZING_RAIN = 'ZR'  # weather code ("Freezing Rain")
    CLOUDY = 'cloudy'
    SUNNY = 'sunny'
