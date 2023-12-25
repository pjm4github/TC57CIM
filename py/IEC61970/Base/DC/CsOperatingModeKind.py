# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from enum import Enum

class CsOperatingModeKind(Enum):
    """
    Operating mode for HVDC line operating as Current Source Converter.
    @author selaost1
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """
    INVERTER = 0  # "Operating as inverter"
    RECTIFIER = 1  # "Operating as rectifier"
