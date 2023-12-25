# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PerLengthImpedance import PerLengthImpedance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseImpedanceData import PhaseImpedanceData


class PerLengthPhaseImpedance(PerLengthImpedance):

    def __init__(self) -> None:
        super().__init__()
        self._phase_impedance_data = PhaseImpedanceData()

    def get_conductor_count(self) -> int:
        return self._conductor_count

    def get_phase_impedance_data(self) -> PhaseImpedanceData:
        return self._phase_impedance_data

    def set_conductor_count(self, new_val: int) -> None:
        self._conductor_count = new_val

    def set_phase_impedance_data(self, new_val: PhaseImpedanceData) -> None:
        self._phase_impedance_data = new_val
