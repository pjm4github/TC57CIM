# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerLinear(PhaseTapChanger):

    def __init__(self):
        super().__init__()
        self.step_phase_shift_increment = AngleDegrees()
        self.x_max = Reactance()
        self.x_min = Reactance()

    def get_step_phase_shift_increment(self) -> AngleDegrees:
        return self.step_phase_shift_increment

    def get_x_max(self) -> Reactance:
        return self.x_max

    def get_x_min(self) -> Reactance:
        return self.x_min

    def set_step_phase_shift_increment(self, new_val: AngleDegrees):
        self.step_phase_shift_increment = new_val

    def set_x_max(self, new_val: Reactance):
        self.x_max = new_val

    def set_x_min(self, new_val: Reactance):
        self.x_min = new_val
