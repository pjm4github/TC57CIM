# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingControl import RegulatingControl


class TapChangerControl(RegulatingControl):

    def __init__(self):
        super().__init__()
        self.limit_voltage: Optional[Voltage] = Voltage()  # Maximum allowed regulated voltage on the PT secondary, regardless of line drop compensation
        self.line_drop_compensation: bool = False  # If true, the line drop compensation is to be applied
        self.line_drop_r: Optional[Resistance] = Resistance()  # Line drop compensator resistance setting for normal (forward) power flow
        self.line_drop_x: Optional[Reactance] = Reactance()  # Line drop compensator reactance setting for normal (forward) power flow
        self.reverse_line_drop_r: Optional[Resistance] = Resistance()  # Line drop compensator resistance setting for reverse power flow
        self.reverse_line_drop_x: Optional[Reactance] = Reactance()  # Line drop compensator reactance setting for reverse power flow

    def get_limit_voltage(self) -> Voltage:
        return self.limit_voltage

    def get_line_drop_compensation(self) -> bool:
        return self.line_drop_compensation

    def get_line_drop_r(self) -> Resistance:
        return self.line_drop_r

    def get_line_drop_x(self) -> Reactance:
        return self.line_drop_x

    def get_reverse_line_drop_r(self) -> Resistance:
        return self.reverse_line_drop_r

    def get_reverse_line_drop_x(self) -> Reactance:
        return self.reverse_line_drop_x

    def set_limit_voltage(self, new_val: Voltage):
        self.limit_voltage = new_val

    def set_line_drop_compensation(self, new_val: bool):
        self.line_drop_compensation = new_val

    def set_line_drop_r(self, new_val: Resistance):
        self.line_drop_r = new_val

    def set_line_drop_x(self, new_val: Reactance):
        self.line_drop_x = new_val

    def set_reverse_line_drop_r(self, new_val: Resistance):
        self.reverse_line_drop_r = new_val

    def set_reverse_line_drop_x(self, new_val: Reactance):
        self.reverse_line_drop_x = new_val
