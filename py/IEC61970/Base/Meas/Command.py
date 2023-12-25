# Command.py
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.Control import Control
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.ValueAliasSet import ValueAliasSet


class Command(Control):
    def __init__(self):
        super().__init__()
        self.normalValue = 0
        self.value = 0
        self.ValueAliasSet = ValueAliasSet()

