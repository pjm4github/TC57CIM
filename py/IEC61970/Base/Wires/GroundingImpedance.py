# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.EarthFaultCompensator import EarthFaultCompensator


class GroundingImpedance(EarthFaultCompensator):
    """
    A fixed impedance device used for grounding.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self):
        super().__init__()
        self.x = Reactance()

    def get_x(self) -> Reactance:
        return self.x

    def set_x(self, new_val: Reactance) -> None:
        self.x = new_val
