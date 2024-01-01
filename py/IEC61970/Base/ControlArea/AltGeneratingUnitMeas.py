# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:02:59 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Meas.AnalogValue import AnalogValue


class AltGeneratingUnitMeas(IdentifiedObject):
    """
    A prioritized measurement to be used for the generating unit in the control area specification.
    """

    def __init__(self) -> None:
        super().__init__()
        self.priorityOptional[int] = 0  # Priority of a measurement usage. Lower numbers have first priority.
        self.analog_valueOptional[AnalogValue] = AnalogValue()  # The specific analog value used as a source.
