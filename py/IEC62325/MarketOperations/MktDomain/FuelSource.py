# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class FuelSource(Enum):
    NG = 1  # Natural Gas
    NNG = 2  # Non-Natural Gas
    BGAS = 3  # Bio Gas (Landfill, Sewage, Digester, etc.)
    BIOM = 4  # Biomass
    COAL = 5  # Coal
    DIST = 6  # DIST
    GAS = 7  # Natural Gas
    GEOT = 8  # GeoThermal
    HRCV = 9  # HRCV
    NONE = 10  # None
    NUCL = 11  # Nuclear
    OIL = 12  # Oil
    OTHR = 13  # Other
    SOLR = 14  # Solar
    WAST = 15  # Waste to Energy
    WATR = 16  # Water
    WIND = 17  # Wind
