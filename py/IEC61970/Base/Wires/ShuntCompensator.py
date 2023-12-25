# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from datetime import datetime
from typing import Optional, Union

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.VoltagePerReactivePower import VoltagePerReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseShuntConnectionKind import PhaseShuntConnectionKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ShuntCompensatorPhase import ShuntCompensatorPhase


class ShuntCompensator:

    def __init__(self):
        self.a_vr_delay: Optional[Seconds] = Seconds() # Time delay required for the device to be connected or disconnected by AVR
        self.grounded: bool = False # Used for Yn and Zn connections. True if the neutral is solidly grounded.
        self.maximum_sections: Optional[int] = 0 # The maximum number of sections that may be switched in
        self.nom_u: Optional[Voltage] = Voltage() # The voltage at which the nominal reactive power may be calculated
        self.normal_sections: Optional[int] = 0 # The normal number of sections switched in
        self.phase_connection: Optional[PhaseShuntConnectionKind] = PhaseShuntConnectionKind.D # The type of phase connection, such as wye or delta
        self.sections: Optional[float] = 0.0 # Shunt compensator sections in use
        self.shunt_compensator_phase: Optional[ShuntCompensatorPhase] = ShuntCompensatorPhase() # The individual phases models for the shunt compensator
        self.switch_on_count: int = 0 # The switch on count since the capacitor count was last reset or initialized
        self.switch_on_date: Optional[datetime] = datetime.now() # The date and time when the capacitor bank was last switched on
        self.voltage_sensitivity: Optional[VoltagePerReactivePower] = VoltagePerReactivePower() # Voltage sensitivity required for the device to regulate the bus voltage

    def set_a_vr_delay(self, new_val: float):
        self.a_vr_delay = new_val

    def set_grounded(self, new_val: bool):
        self.grounded = new_val

    def set_maximum_sections(self, new_val: int):
        self.maximum_sections = new_val

    def set_nom_u(self, new_val: float):
        self.nom_u = new_val

    def set_normal_sections(self, new_val: int):
        self.normal_sections = new_val

    def set_phase_connection(self, new_val: str):
        self.phase_connection = new_val

    def set_sections(self, new_val: float):
        self.sections = new_val

    def set_shunt_compensator_phase(self, new_val: Union[str, float]):
        self.shunt_compensator_phase = new_val

    def set_switch_on_count(self, new_val: int):
        self.switch_on_count = new_val

    def set_switch_on_date(self, new_val: datetime):
        self.switch_on_date = new_val

    def set_voltage_sensitivity(self, new_val: float):
        self.voltage_sensitivity = new_val

    def get_a_vr_delay(self) -> Optional[float]:
        return self.a_vr_delay

    def get_grounded(self) -> bool:
        return self.grounded

    def get_maximum_sections(self) -> int:
        return self.maximum_sections

    def get_nom_u(self) -> Optional[float]:
        return self.nom_u

    def get_normal_sections(self) -> int:
        return self.normal_sections

    def get_phase_connection(self) -> Optional[str]:
        return self.phase_connection

    def get_sections(self) -> float:
        return self.sections

    def get_shunt_compensator_phase(self) -> Union[str, float]:
        return self.shunt_compensator_phase

    def get_switch_on_count(self) -> int:
        return self.switch_on_count

    def get_switch_on_date(self) -> Optional[datetime]:
        return self.switch_on_date

    def get_voltage_sensitivity(self) -> float:
        return self.voltage_sensitivity
