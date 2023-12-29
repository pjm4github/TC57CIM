# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class UnitType(Enum):
    """Unit type enumeration"""
    COMBINED_CYCLE = 1   # * Combined Cycle
    GAS_TURBINE = 2   # * Gas Turbine
    HYDRO_TURBINE = 3   # * Hydro Turbine
    OTHER = 4   # * Other
    PHOTOVOLTAIC = 5   # * Photovoltaic
    HYDRO_PUMP_TURBINE = 6   # * Hydro Pump-Turbine
    RECIPROCATING_ENGINE = 7   # * Reciprocating Engine
    STEAM_TURBINE = 8   # * Steam Turbine
    SYNCHRONOUS_CONDENSER = 9   # * Synchronous Condenser
    WIND_TURBINE = 10   # * Wind Turbine
