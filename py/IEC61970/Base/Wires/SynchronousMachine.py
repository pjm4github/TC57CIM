# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from datetime import timedelta
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PU import PU
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.CoolantType import CoolantType
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RotatingMachine import RotatingMachine
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ShortCircuitRotorKind import ShortCircuitRotorKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SynchronousMachineKind import SynchronousMachineKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SynchronousMachineOperatingMode import SynchronousMachineOperatingMode


class SynchronousMachine(RotatingMachine):

    def __init__(self):
        super().__init__()
        self.a_vr_to_manual_lag: Optional[timedelta] = timedelta()
        self.a_vr_to_manual_lead: Optional[timedelta] = timedelta()
        self.base_q: Optional[ReactivePower] = ReactivePower()
        self.condenser_p: Optional[ActivePower] = ActivePower()
        self.coolant_condition: Optional[float] = 0.0
        self.coolant_type: Optional[CoolantType] = CoolantType.WATER
        self.earthing: Optional[bool] = True
        self.earthing_star_point_r: Optional[Resistance] = Resistance()
        self.earthing_star_point_x: Optional[Reactance] = Reactance()
        self.ikk: Optional[CurrentFlow] = CurrentFlow()
        self.manual_to_avr: Optional[timedelta] = timedelta()
        self.max_q: Optional[ReactivePower] = ReactivePower()
        self.max_u: Optional[Voltage] = Voltage()
        self.min_q: Optional[ReactivePower] = ReactivePower()
        self.min_u: Optional[Voltage] = Voltage()
        self.mu: Optional[float] = 1.0
        self.operating_mode: Optional[SynchronousMachineOperatingMode] = SynchronousMachineOperatingMode.motor
        self.q_percent: Optional[PerCent] = PerCent()
        self.r: Optional[Resistance] = Resistance()
        self.r0: Optional[Resistance] = Resistance()
        self.r2: Optional[Resistance] = Resistance()
        self.reference_priority: Optional[int] = 0
        self.sat_direct_subtrans_x: Optional[PU] = PU()
        self.sat_direct_sync_x: Optional[PU] = PU()
        self.sat_direct_trans_x: Optional[PU] = PU()
        self.short_circuit_rotor_type: Optional[ShortCircuitRotorKind] = ShortCircuitRotorKind.SALIENT_POLE_1
        self.type: Optional[SynchronousMachineKind] = SynchronousMachineKind.MOTOR
        self.voltage_regulation_range: Optional[PerCent] = PerCent()
        self.x0: Optional[Reactance] = Reactance()
        self.x2: Optional[Reactance] = Reactance()

    def get_a_vr_to_manual_lag(self) -> Optional[Seconds]:
        return self.a_vr_to_manual_lag

    def get_a_vr_to_manual_lead(self) -> Optional[Seconds]:
        return self.a_vr_to_manual_lead

    def get_base_q(self) -> Optional[ReactivePower]:
        return self.base_q

    def get_condenser_p(self) -> Optional[ActivePower]:
        return self.condenser_p

    def get_coolant_condition(self) -> Optional[float]:
        return self.coolant_condition

    def get_coolant_type(self) -> Optional[CoolantType]:
        return self.coolant_type

    def get_earthing(self) -> Optional[bool]:
        return self.earthing

    def get_earthing_star_point_r(self) -> Optional[Resistance]:
        return self.earthing_star_point_r

    def get_earthing_star_point_x(self) -> Optional[Reactance]:
        return self.earthing_star_point_x

    # Implement other getters similarly

    def set_a_vr_to_manual_lag(self, new_val: Seconds) -> None:
        self.a_vr_to_manual_lag = new_val

    def set_a_vr_to_manual_lead(self, new_val: Seconds) -> None:
        self.a_vr_to_manual_lead = new_val

    def set_base_q(self, new_val: ReactivePower) -> None:
        self.base_q = new_val

    def set_condenser_p(self, new_val: ActivePower) -> None:
        self.condenser_p = new_val

    def set_coolant_condition(self, new_val: float) -> None:
        self.coolant_condition = new_val

    def set_coolant_type(self, new_val: CoolantType) -> None:
        self.coolant_type = new_val

    def set_earthing(self, new_val: bool) -> None:
        self.earthing = new_val

    def set_earthing_star_point_r(self, new_val: Resistance) -> None:
        self.earthing_star_point_r = new_val

    def set_earthing_star_point_x(self, new_val: Reactance) -> None:
        self.earthing_star_point_x = new_val

    # Implement other setters similarly
