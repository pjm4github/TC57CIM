# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.EnergyConnection import EnergyConnection
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingControl import RegulatingControl


class RegulatingCondEq(EnergyConnection):

    def __init__(self):
        super().__init__()
        self.control_enabled = False
        self.regulating_control = RegulatingControl()

    def get_control_enabled(self) -> bool:
        return self.control_enabled

    def get_regulating_control(self) -> RegulatingControl:
        return self.regulating_control

    def set_control_enabled(self, new_val: bool):
        self.control_enabled = new_val

    def set_regulating_control(self, new_val: RegulatingControl):
        self.regulating_control = new_val

