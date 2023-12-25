# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind


class EnergyConsumerPhase:
    def __init__(self) -> None:
        self.p: ActivePower = ActivePower()
        self.pfixed: ActivePower = ActivePower()
        self.pfixed_pct: PerCent = PerCent()
        self.phase: SinglePhaseKind = SinglePhaseKind.N
        self.q: ReactivePower = ReactivePower()
        self.qfixed: ReactivePower = ReactivePower()
        self.qfixed_pct: PerCent = PerCent()

    def get_p(self) -> ActivePower:
        return self.p

    def get_pfixed(self) -> ActivePower:
        return self.pfixed

    def get_pfixed_pct(self) -> PerCent:
        return self.pfixed_pct

    def get_phase(self) -> SinglePhaseKind:
        return self.phase

    def get_q(self) -> ReactivePower:
        return self.q

    def get_qfixed(self) -> ReactivePower:
        return self.qfixed

    def get_qfixed_pct(self) -> PerCent:
        return self.qfixed_pct

    def set_p(self, new_val: ActivePower) -> None:
        self.p = new_val

    def set_pfixed(self, new_val: ActivePower) -> None:
        self.pfixed = new_val

    def set_pfixed_pct(self, new_val: PerCent) -> None:
        self.pfixed_pct = new_val

    def set_phase(self, new_val: SinglePhaseKind) -> None:
        self.phase = new_val

    def set_q(self, new_val: ReactivePower) -> None:
        self.q = new_val

    def set_qfixed(self, new_val: ReactivePower) -> None:
        self.qfixed = new_val

    def set_qfixed_pct(self, new_val: PerCent) -> None:
        self.qfixed_pct = new_val
