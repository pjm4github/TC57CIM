# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
"""
Analogs representing oil moisture analysis result.
@author ppbr003
@version 1.0
@created 20-Dec-2023 10:57:27 AM
"""

from enum import Enum

class OilAnalysisMoistureAnalogKind(Enum):
    WATER_CONTENT = 1  # MOISTURE MEASURED VIA COULometric Karl Fischer titration (in ppm, specifically milligram/kilogram).
    WATER_CONTENT_MONITORED_VIA_INFRARED = 2  # WATer content by infrared sensor (in ppm, specifically milligram/kilogram).
    WATER_CONTENT_MONITORED_VIA_CAPACITANCE = 3  # Water content by capacitance sensor (in ppm, specifically milligram/kilogram).
    WATER_CONTENT_MONITORED_VIA_ALUMINUM_OXIDE = 4  # Water content by aluminum oxide sensor (in ppm, specifically milligram/kilogram).
    WATER_CONTENT_MONITORED_VIA_OTHER = 5  # WATER content by other sensor (in ppm, specifically milligram/kilogram).
    RELATIVE_SATURATION = 6  # RELATIVE SATURATION of water in fluid (in percent).
    RELATIVE_SATURATION_CALCULATED = 7  # CALCULATEd relative saturation of water in fluid (in percent).
    DEW_POINT = 8  # DEW POINT (IN CELSIUS). IS USUally a negative value.
