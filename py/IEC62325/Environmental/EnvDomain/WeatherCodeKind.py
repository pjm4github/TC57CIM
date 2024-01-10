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

    HAIL = 'A'  # weather code1 ("Hail")
    BLOWING_DUST = 'BD'  # weather code1 ("Blowing Dust")
    BLOWING_SAND = 'BN'  # weather code1 ("Blowing Sand")
    MIST = 'BR'  # weather code1 ("Mist")
    BLOWING_SNOW = 'BS'  # weather code1 ("Blowing Snow")
    FOG = 'F'  # weather code1 ("Fog")
    FROST = 'FR'  # weather code1 ("Frost")
    HAZE = 'H'  # weather code1 ("Haze")
    ICE_CRYSTALS = 'IC'  # weather code1 ("Ice Crystals")
    ICE_FOG = 'IF'  # weather code1 ("Ice Fog")
    SLEET = 'IP'  # weather code1 ("Ice Pellets/Sleet")
    SMOKE = 'K'  # weather code1 ("Smoke")
    DRIZZLE = 'L'  # weather code1 ("Drizzle")
    RAIN = 'R'  # weather code1 ("Rain")
    RAIN_SHOWERS = 'RW'  # weather code1 ("Rain Showers")
    RAIN_SNOW_MIX = 'RS'  # weather code1 ("Rain/Snow Mix")
    SNOW_SLEET_MIX = 'SI'  # weather code1 ("Snow/Sleet Mix")
    WINTRY_MIX = 'WS'  # weather code1 ("Wintry Mix")
    SNOW = 'S'  # weather code1 ("Snow")
    SNOW_SHOWERS = 'SW'  # weather code1 ("Snow Showers")
    THUNDER_STORMS = 'T'  # weather code1 ("Thunderstorms")
    VOLCANIC_ASH = 'VA'  # weather code1 ("Volcanic Ash")
    WATER_SPOUTS = 'WP'  # weather code1 ("Water Spouts")
    FREEZING_SPRAY = 'ZF'  # weather code1 ("Freezing Spray")
    FREEZING_DRIZZLE = 'ZL'  # weather code1 ("Freezing Drizzle")
    FREEZING_RAIN = 'ZR'  # weather code1 ("Freezing Rain")
    CLOUDY = 'cloudy'
    SUNNY = 'sunny'
