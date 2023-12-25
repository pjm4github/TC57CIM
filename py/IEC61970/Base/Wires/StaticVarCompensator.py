# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any, Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.VoltagePerReactivePower import VoltagePerReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingCondEq import RegulatingCondEq
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SVCControlMode import SVCControlMode


class StaticVarCompensator(RegulatingCondEq):
    """
    A facility for providing variable and controllable shunt reactive power. The
    SVC typically consists of a stepdown transformer, filter, thyristor-controlled
    reactor, and thyristor-switched capacitor arms.
    The SVC may operate in fixed MVar output mode or in voltage control mode. When
    in voltage control mode, the output of the SVC will be proportional to the
    deviation of voltage at the controlled bus from the voltage setpoint. The SVC
    characteristic slope defines the proportion. If the voltage at the controlled
    bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """

    def __init__(self) -> None:
        """Constructor"""

        super().__init__()
        self.capacitive_rating: Optional[Reactance] = Reactance()
        self.inductive_rating: Optional[Reactance] = Reactance()
        self.q: Optional[ReactivePower] = ReactivePower()
        self.slope: Optional[VoltagePerReactivePower] = VoltagePerReactivePower()
        self.svc_control_mode: Optional[SVCControlMode] = SVCControlMode.VOLTAGE
        self.voltage_set_point: Optional[Voltage] = Voltage()

    def get_capacitive_rating(self) -> Optional[Reactance]:
        return self.capacitive_rating

    def get_inductive_rating(self) -> Optional[Reactance]:
        return self.inductive_rating

    def get_q(self) -> Optional[ReactivePower]:
        return self.q

    def get_slope(self) -> Optional[VoltagePerReactivePower]:
        return self.slope

    def get_sVC_control_mode(self) -> Optional[SVCControlMode]:
        return self.svc_control_mode

    def get_voltage_set_point(self) -> Optional[Voltage]:
        return self.voltage_set_point

    def set_capacitive_rating(self, new_val: Reactance) -> None:
        self.capacitive_rating = new_val

    def set_inductive_rating(self, new_val: Reactance) -> None:
        self.inductive_rating = new_val

    def set_q(self, new_val: ReactivePower) -> None:
        self.q = new_val

    def set_slope(self, new_val: VoltagePerReactivePower) -> None:
        self.slope = new_val

    def set_sVC_control_mode(self, new_val: SVCControlMode) -> None:
        self.svc_control_mode = new_val

    def set_voltage_set_point(self, new_val: Voltage) -> None:
        self.voltage_set_point = new_val
