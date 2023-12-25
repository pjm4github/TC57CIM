# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from dataclasses import dataclass
from typing import Optional, Union

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePowerPerFrequency import ActivePowerPerFrequency
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PU import PU
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingCondEq import RegulatingCondEq


@dataclass
class ExternalNetworkInjection(RegulatingCondEq):
    """
    This class represents external network and it is used for IEC 60909 calculations.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """
    def __init__(self):
        super().__init__()
        # Power Frequency Bias. This is the change in power injection divided by the change in frequency and negated.
        # A positive value of the power frequency bias provides additional power injection upon a drop in frequency.
        self.governor_scd: Optional[ActivePowerPerFrequency] = ActivePowerPerFrequency()
        self.ik_second: bool = False  # Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik").
        self.max_initial_sym_shc_current: Optional[CurrentFlow] = CurrentFlow()  # Maximum initial symmetrical short-circuit currents (Ik" max) in A (Ik" = Sk"/(SQRT(3) Un)).
        self.max_p: Optional[ActivePower] = ActivePower()  # Maximum active power of the injection.
        self.max_q: Optional[ReactivePower] = ReactivePower()  # Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used
        self.max_r0_to_x0_ratio: float = 0.0  # Maximum ratio of zero sequence resistance of Network Feeder to its zero sequence reactance (R(0)/X(0) max). Used for short circuit data exchange
        self.max_r1_to_x1_ratio: float = 0.0  # Maximum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) max). Used for short circuit data exchange
        self.max_z0_to_z1_ratio: float = 0.0  # Maximum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) max). Used for short circuit data exchange according to IEC 60909
        self.min_initial_sym_shc_current: Optional[CurrentFlow] = CurrentFlow()  # Minimum initial symmetrical short-circuit currents (Ik" min) in A (Ik" = Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909
        self.min_p: Optional[ActivePower] = ActivePower()  # Minimum active power of the injection.
        self.min_q: Optional[ReactivePower] = ReactivePower()  # Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used
        self.min_r0_to_x0_ratio: float = 0.0  # Minimum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) min). Used for short circuit data exchange according to IEC 60909
        self.min_r1_to_x1_ratio: float = 0.0  # Minimum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) min). Used for short circuit data exchange
        self.p: Optional[ActivePower] = ActivePower()  # Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions.
        self.q: Optional[ReactivePower] = ReactivePower()  # Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions.
        self.reference_priority: int = 0  # Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don't care (default) 1 = highest priority. 2 is less than 1 and so on.
        self.voltage_factor: Optional[PU] = PU()  # Voltage factor in pu, which was used to calculate short-circuit current Ik" and power Sk".

    def set_governor_scd(self, new_val: ActivePowerPerFrequency):
        self.governor_scd = new_val

    def set_ik_second(self, new_val: bool):
        self.ik_second = new_val

    def set_max_initial_sym_shc_current(self, new_val: CurrentFlow):
        self.max_initial_sym_shc_current = new_val

    def set_max_p(self, new_val: ActivePower):
        self.max_p = new_val

    def set_max_q(self, new_val: ReactivePower):
        self.max_q = new_val

    def set_max_r0_to_x0_ratio(self, new_val: float):
        self.max_r0_to_x0_ratio = new_val

    def set_max_r1_to_x1_ratio(self, new_val: float):
        self.max_r1_to_x1_ratio = new_val

    def set_max_z0_to_z1_ratio(self, new_val: float):
        self.max_z0_to_z1_ratio = new_val

    def set_min_initial_sym_shc_current(self, new_val: CurrentFlow):
        self.min_initial_sym_shc_current = new_val

    def set_min_p(self, new_val: ActivePower):
        self.min_p = new_val

    def set_min_q(self, new_val: ReactivePower):
        self.min_q = new_val

    def set_min_r0_to_x0_ratio(self, new_val: float):
        self.min_r0_to_x0_ratio = new_val

    def set_min_r1_to_x1_ratio(self, new_val: float):
        self.min_r1_to_x1_ratio = new_val

    def set_min_z0_to_z1_ratio(self, new_val: float):
        self.min_z0_to_z1_ratio = new_val

    def set_p(self, new_val: ActivePower):
        self.p = new_val

    def set_q(self, new_val: ReactivePower):
        self.q = new_val

    def set_reference_priority(self, new_val: int):
        self.reference_priority = new_val

    def set_voltage_factor(self, new_val: PU):
        self.voltage_factor = new_val

    def get_governor_scd(self) -> Optional[ActivePowerPerFrequency]:
        return self.governor_scd

    def get_ik_second(self) -> bool:
        return self.ik_second

    def get_max_initial_sym_shc_current(self) -> Optional[CurrentFlow]:
        return self.max_initial_sym_shc_current

    def get_max_p(self) -> Optional[ActivePower]:
        return self.max_p

    def get_max_q(self) -> Optional[ReactivePower]:
        return self.max_q

    def get_max_r0_to_x0_ratio(self) -> float:
        return self.max_r0_to_x0_ratio

    def get_max_r1_to_x1_ratio(self) -> float:
        return self.max_r1_to_x1_ratio

    def get_max_z0_to_z1_ratio(self) -> float:
        return self.max_z0_to_z1_ratio

    def get_min_initial_sym_shc_current(self) -> Optional[CurrentFlow]:
        return self.min_initial_sym_shc_current

    def get_min_p(self) -> Optional[ActivePower]:
        return self.min_p

    def get_min_q(self) -> Optional[ReactivePower]:
        return self.min_q

    def get_min_r0_to_x0_ratio(self) -> float:
        return self.min_r0_to_x0_ratio

    def get_min_r1_to_x1_ratio(self) -> float:
        return self.min_r1_to_x1_ratio

    def get_min_z0_to_z1_ratio(self) -> float:
        return self.min_z0_to_z1_ratio

    def get_p(self) -> Optional[ActivePower]:
        return self.p

    def get_q(self) -> Optional[ReactivePower]:
        return self.q

    def get_reference_priority(self) -> int:
        return self.reference_priority

    def get_voltage_factor(self) -> Optional[PU]:
        return self.voltage_factor
