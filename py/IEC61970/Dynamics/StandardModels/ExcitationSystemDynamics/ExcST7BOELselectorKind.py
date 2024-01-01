# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from enum import Enum


class ExcST7BOELselectorKind(Enum):
    """
    Type of connection for the OEL input used for static excitation systems type 7B.
    """
    NO_OEL_INPUT = 1  # No OEL input is used.
    ADD_VREF = 2  # The signal is added to Vref.
    INPUT_LV_GATE = 3  # The signal is connected in the input of the LV gate.
    OUTPUT_LV_GATE = 4  # The signal is connected in the output of the LV gate.
