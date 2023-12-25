# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.LoadModel.LoadResponseCharacteristic import LoadResponseCharacteristic
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.EnergyConnection import EnergyConnection
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.EnergyConsumerPhase import EnergyConsumerPhase
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseShuntConnectionKind import PhaseShuntConnectionKind


class EnergyConsumer(EnergyConnection):
    """
    Generic user of energy - a point of consumption on the power system model.
    @author pmora
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.customer_count: int = 0
        self.grounded: bool = False
        self.p: Optional[ActivePower] = ActivePower()
        self.p_fixed: Optional[ActivePower] = ActivePower()
        self.p_fixed_pct: Optional[PerCent] = PerCent()
        self.phase_connection: Optional[PhaseShuntConnectionKind] = PhaseShuntConnectionKind.D
        self.q: Optional[ReactivePower] = ReactivePower()
        self.q_fixed: Optional[ReactivePower] = ReactivePower()
        self.q_fixed_pct: Optional[PerCent] = PerCent()
        self.energy_consumer_phase: Optional[EnergyConsumerPhase] = EnergyConsumerPhase()
        self.load_response = LoadResponseCharacteristic()

    def get_customer_count(self) -> int:
        return self.customer_count

    def get_energy_consumer_phase(self) -> Optional[EnergyConsumerPhase]:
        return self.energy_consumer_phase

    def get_grounded(self) -> bool:
        return self.grounded

    def get_load_response(self) -> LoadResponseCharacteristic:
        return self.load_response

    def get_p(self) -> Optional[ActivePower]:
        return self.p

    def get_p_fixed(self) -> Optional[ActivePower]:
        return self.p_fixed

    def get_p_fixed_pct(self) -> Optional[PerCent]:
        return self.p_fixed_pct

    def get_phase_connection(self) -> Optional[PhaseShuntConnectionKind]:
        return self.phase_connection

    def get_q(self) -> Optional[ReactivePower]:
        return self.q

    def get_q_fixed(self) -> Optional[ReactivePower]:
        return self.q_fixed

    def get_q_fixed_pct(self) -> Optional[PerCent]:
        return self.q_fixed_pct

    def set_customer_count(self, new_val: int) -> None:
        self.customer_count = new_val

    def set_energy_consumer_phase(self, new_val: EnergyConsumerPhase) -> None:
        self.energy_consumer_phase = new_val

    def set_grounded(self, new_val: bool) -> None:
        self.grounded = new_val

    def set_load_response(self, new_val: LoadResponseCharacteristic) -> None:
        self.load_response = new_val

    def set_p(self, new_val: ActivePower) -> None:
        self.p = new_val

    def set_p_fixed(self, new_val: ActivePower) -> None:
        self.p_fixed = new_val

    def set_p_fixed_pct(self, new_val: PerCent) -> None:
        self.p_fixed_pct = new_val

    def set_phase_connection(self, new_val: PhaseShuntConnectionKind) -> None:
        self.phase_connection = new_val

    def set_q(self, new_val: ReactivePower) -> None:
        self.q = new_val

    def set_q_fixed(self, new_val: ReactivePower) -> None:
        self.q_fixed = new_val

    def set_q_fixed_pct(self, new_val: PerCent) -> None:
        self.q_fixed_pct = new_val
