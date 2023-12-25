# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 16:45:14 2023
from enum import Enum

class ShortCircuitRotorKind(Enum):
    """
    Type of rotor, used by short circuit applications.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    SALIENT_POLE_1 = 1  # Salient pole 1 in the IEC 60909
    SALIENT_POLE_2 = 2  # Salient pole 2 in IEC 60909
    TURBO_SERIES_1 = 3  # Turbo Series 1 in the IEC 60909
    TURBO_SERIES_2 = 4  # Turbo series 2 in IEC 60909
