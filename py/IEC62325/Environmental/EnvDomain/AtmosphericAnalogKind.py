# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# This class defines the kinds of analogs (floats) measuring an atmospheric condition
# Author: ppbr003
# Version: 1.0
# Created: 25-Dec-2023 9:21:22 PM
from enum import Enum


class AtmosphericAnalogKind(Enum):
    ALBEDO = 1
    # The temperature measured by a thermometer exposed to the air in a place sheltered from direct solar radiation.
    # Also known as "dry bulb" because the air temperature is indicated by a thermometer not affected
    # by the moisture of the air.
    AMBIENT_TEMPERATURE = 2
    ATMOSPHERIC_PRESSURE = 3
    CEILING = 4
    # The temperature to which air must be cooled at constant pressure and constant water-vapor content
    # in order for saturation to occur.
    # In other words, it is the temperature at which water vapor starts to condense out of the air.
    DEW_POINT = 5
    # The temperature of how hot it "feels like" for a given combination of warm air temperature and relative humidity.
    HEAT_INDEX = 6
    HORIZONTAL_VISIBILITY = 7
    HUMIDITY = 8
    ICE = 9
    ILLUMINANCE_DIFFUSE_HORIZONTAL = 10
    ILLUMINANCE_DIRECT_NORMAL = 11
    ILLUMINANCE_GLOBAL_HORIZONTAL = 12
    IRRADIANCE_DIFFUSE_HORIZONTAL = 13
    IRRADIANCE_DIRECT_NORMAL = 14
    IRRADIANCE_EXTRA_TERRESTRIAL_HORIZONTAL = 15
    IRRADIANCE_EXTRA_TERRESTRIAL_VERTICAL = 16
    IRRADIANCE_GLOBAL_HORIZONTAL = 17
    LUMINANCE_ZENITH = 18
    PRECIPITATION = 19
    RAIN = 20
    SKY_COVERAGE_OPAQUE = 21
    SKY_COVERAGE_TOTAL = 22
    # Snow amount over a specified period of time.
    SNOW = 23
    # The temperature of how cold it "feels like" based on the rate of heat loss from exposed skin
    # caused by the effects of wind and cold temperatures.
    WIND_CHILL = 24
    # Maximum instantaneous wind speed in the 10-minute period preceding a moment in time so long as more
    # than 10 knots of difference has been exhibited between peaks and lulls during that 10-minute time period.
    # 0 value means no gusts during the preceding 10-minute period.
    WIND_SPEED_GUST = 25
    # Wind speed at a moment in time.
    WIND_SPEED_INSTANTANEOUS = 26
    # Peak instantaneous wind speed in the 60 minutes preceding a moment in time as long as peak
    # speed greater than 25 knots.
    # 0 value means speed did not exceed 25 knots during preceding 60 minutes.
    WIND_SPEED_PEAK = 27
    # Average instantaneous wind speed over the 2-minute time period preceding a moment in time.
    WIND_SPEED_SUSTAINED = 28
    VERTICAL_VISIBILITY = 29


