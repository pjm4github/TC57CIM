# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from enum import StrEnum


class FuelType(StrEnum):
    """
    Type of fuel.
    @created 02-Jan-2024 11:00:26 PM
    """
    COAL = "coal"  # Generic coal, not including lignite type.
    OIL = "oil"  # Oil.
    GAS = "gas"  # Natural gas.
    LIGNITE = "lignite"  # The fuel is lignite coal. Note that this is a special type of coal, so the
    # other enum of coal is reserved for hard coal types or if the exact type of coal
    # is not known.
    HARD_COAL = "hardCoal"  # Hard coal
    OIL_SHALE = "oilShale"  # Oil Shale
    GASOLINE = "gasoline"