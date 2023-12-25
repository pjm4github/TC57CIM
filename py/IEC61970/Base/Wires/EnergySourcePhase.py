# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.EnergySource import EnergySource
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind


class EnergySourcePhase:
    """
    Represents the single phase information of an unbalanced energy source.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        self.energy_source = EnergySource()
        self.phase = SinglePhaseKind.N

    def get_energy_source(self) -> EnergySource:
        return self.energy_source

    def get_phase(self) -> SinglePhaseKind:
        return self.phase

    def set_energy_source(self, new_val: EnergySource) -> None:
        self.energy_source = new_val

    def set_phase(self, new_val: SinglePhaseKind) -> None:
        self.phase = new_val
