# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:38:50 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas import Control
from typing import Optional

class AnalogControl(Control):
    """
    An analog control used for supervisory control.
    @author selaost1
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        self.max_value: Optional[float] = 0.0  # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
        self.min_value: Optional[float] = 0.0  # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
