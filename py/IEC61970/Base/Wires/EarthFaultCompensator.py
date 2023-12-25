# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance


class EarthFaultCompensator:
    """
    A conducting equipment used to represent a connection to ground which is typically used to compensate earth faults. An earth fault compensator device modeled with a single terminal implies a second terminal solidly connected to ground. If two terminals are modeled, the ground is not assumed and normal connection rules apply.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        self.r: Resistance

    def get_r(self) -> Resistance:
        return self.r

    def set_r(self, new_val: Resistance) -> None:
        self.r = new_val
