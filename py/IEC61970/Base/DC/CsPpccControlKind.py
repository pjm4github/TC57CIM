# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from enum import Enum

class CsPpccControlKind(Enum):
    """
    Active power control modes for HVDC line operating as Current Source Converter.
    @author selaost1
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    ACTIVE_POWER = 1  # Active power control at AC side.
    DC_VOLTAGE = 2  # DC voltage control.
    DC_CURRENT = 3  # DC current control
