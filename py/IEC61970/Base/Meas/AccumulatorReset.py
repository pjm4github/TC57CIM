# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:38:50 2023
from datetime import datetime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.Control import  Control
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.AccumulatorValue import AccumulatorValue

class AccumulatorReset(Control):

    # The accumulator value that is reset by the command.

    def __init__(self) -> None:
        super().__init__()
        self.accumulator_value: AccumulatorValue = AccumulatorValue()
