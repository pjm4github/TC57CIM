# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from enum import Enum


class ExcST7BUELselectorKind(Enum):
    """
    Type of connection for the UEL input used for static excitation systems type 7B.
    """
    NO_UEL_INPUT = 0  # No UEL input is used.
    ADD_VREF = 1  # The signal is added to Vref.
    INPUT_HV_GATE = 2  # The signal is connected in the input of the HV gate.
    OUTPUT_HV_GATE = 3  # The signal is connected in the output of the HV gate.
