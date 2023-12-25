# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# from shunt_compensator_phase import ShuntCompensatorPhase
# from susceptance import Susceptance
# from conductance import Conductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Susceptance import Susceptance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.NonlinearShuntCompensatorPhasePoint import Conductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ShuntCompensatorPhase import ShuntCompensatorPhase

class LinearShuntCompensatorPhase(ShuntCompensatorPhase):
    def __init__(self):
        super().__init__()
        self.b_per_section = Susceptance()
        self.g_per_section = Conductance()

    def get_b_per_section(self) -> Susceptance:
        return self.b_per_section

    def get_g_per_section(self) -> Conductance:
        return self.g_per_section

    def set_b_per_section(self, new_val: Susceptance):
        self.b_per_section = new_val

    def set_g_per_section(self, new_val: Conductance):
        self.g_per_section = new_val
