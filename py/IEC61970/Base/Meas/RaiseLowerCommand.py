# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:38:50 2023
from IEC61970.Base.Meas import AnalogControl


class RaiseLowerCommand(AnalogControl):
    """
    An analog control that increase or decrease a set point value with pulses.
    Unless otherwise specified, one pulse moves the set point by one.
    @author selaost1
    @version 1.0
    @created 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        super().__init__()

