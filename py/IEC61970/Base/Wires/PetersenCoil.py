# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.EarthFaultCompensator import EarthFaultCompensator
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PetersenCoilModeKind import PetersenCoilModeKind


class PetersenCoil(EarthFaultCompensator):

    def __init__(self) -> None:
        super().__init__()
        self.mode: PetersenCoilModeKind = PetersenCoilModeKind()
        self.nominal_u: Voltage = Voltage()
        self.offset_current: CurrentFlow = CurrentFlow()
        self.position_current: CurrentFlow = CurrentFlow()
        self.x_ground_max: Reactance = Reactance()
        self.x_ground_min: Reactance = Reactance()
        self.x_ground_nominal: Reactance = Reactance()

    def get_mode(self) -> PetersenCoilModeKind:
        return self.mode

    def get_nominal_u(self) -> Voltage:
        return self.nominal_u

    def get_offset_current(self) -> CurrentFlow:
        return self.offset_current

    def get_position_current(self) -> CurrentFlow:
        return self.position_current

    def get_x_ground_max(self) -> Reactance:
        return self.x_ground_max

    def get_x_ground_min(self) -> Reactance:
        return self.x_ground_min

    def get_x_ground_nominal(self) -> Reactance:
        return self.x_ground_nominal

    def set_mode(self, new_val: PetersenCoilModeKind) -> None:
        self.mode = new_val

    def set_nominal_u(self, new_val: Voltage) -> None:
        self.nominal_u = new_val

    def set_offset_current(self, new_val: CurrentFlow) -> None:
        self.offset_current = new_val

    def set_position_current(self, new_val: CurrentFlow) -> None:
        self.position_current = new_val

    def set_x_ground_max(self, new_val: Reactance) -> None:
        self.x_ground_max = new_val

    def set_x_ground_min(self, new_val: Reactance) -> None:
        self.x_ground_min = new_val

    def set_x_ground_nominal(self, new_val: Reactance) -> None:
        self.x_ground_nominal = new_val
