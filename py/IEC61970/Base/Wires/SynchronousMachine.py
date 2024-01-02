# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from datetime import timedelta
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Reactance import Reactance
from IEC61970.Base.Domain.ReactivePower import ReactivePower
from IEC61970.Base.Domain.Resistance import Resistance
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Voltage import Voltage
from IEC61970.Base.Wires.CoolantType import CoolantType
from IEC61970.Base.Wires.RotatingMachine import RotatingMachine
from IEC61970.Base.Wires.ShortCircuitRotorKind import ShortCircuitRotorKind
from IEC61970.Base.Wires.SynchronousMachineKind import SynchronousMachineKind
from IEC61970.Base.Wires.SynchronousMachineOperatingMode import SynchronousMachineOperatingMode


class SynchronousMachine(RotatingMachine):

    def __init__(self):
        super().__init__()
        self.a_vr_to_manual_lagOptional[timedelta] = timedelta()
        self.a_vr_to_manual_leadOptional[timedelta] = timedelta()
        self.base_qOptional[ReactivePower] = ReactivePower()
        self.condenser_pOptional[ActivePower] = ActivePower()
        self.coolant_conditionfloat = 0.0
        self.coolant_typeOptional[CoolantType] = CoolantType.WATER
        self.earthingbool = True
        self.earthing_star_point_rOptional[Resistance] = Resistance()
        self.earthing_star_point_xOptional[Reactance] = Reactance()
        self.ikkOptional[CurrentFlow] = CurrentFlow()
        self.manual_to_avrOptional[timedelta] = timedelta()
        self.max_qOptional[ReactivePower] = ReactivePower()
        self.max_uOptional[Voltage] = Voltage()
        self.min_qOptional[ReactivePower] = ReactivePower()
        self.min_uOptional[Voltage] = Voltage()
        self.mufloat = 1.0
        self.operating_modeOptional[SynchronousMachineOperatingMode] = SynchronousMachineOperatingMode.motor
        self.q_percentOptional[PerCent] = PerCent()
        self.rOptional[Resistance] = Resistance()
        self.r0Optional[Resistance] = Resistance()
        self.r2Optional[Resistance] = Resistance()
        self.reference_priorityOptional[int] = 0
        self.sat_direct_subtrans_xPU = PU()
        self.sat_direct_sync_xPU = PU()
        self.sat_direct_trans_xPU = PU()
        self.short_circuit_rotor_typeOptional[ShortCircuitRotorKind] = ShortCircuitRotorKind.SALIENT_POLE_1
        self.typeOptional[SynchronousMachineKind] = SynchronousMachineKind.MOTOR
        self.voltage_regulation_rangeOptional[PerCent] = PerCent()
        self.x0Optional[Reactance] = Reactance()
        self.x2Optional[Reactance] = Reactance()

    def get_a_vr_to_manual_lag(self) -> Seconds:
        return self.a_vr_to_manual_lag

    def get_a_vr_to_manual_lead(self) -> Seconds:
        return self.a_vr_to_manual_lead

    def get_base_q(self) -> Optional[ReactivePower]:
        return self.base_q

    def get_condenser_p(self) -> Optional[ActivePower]:
        return self.condenser_p

    def get_coolant_condition(self) -> float:
        return self.coolant_condition

    def get_coolant_type(self) -> Optional[CoolantType]:
        return self.coolant_type

    def get_earthing(self) -> bool:
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
