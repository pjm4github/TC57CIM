# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:41:01 2023
from typing import Optional
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.StateVariable import StateVariable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TapChanger import TapChanger

class SvTapStep(StateVariable):
    """
    State variable for transformer tap step.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        """
        The floating point tap position. This is not the tap ratio, but rather the tap step position as defined by the related tap changer model and normally is constrained to be within the range of minimum and maximum tap positions.
        """
        super().__init__()
        self.position: Optional[float] = 1.0

        """
        The tap changer associated with the tap step state.
        """
        self.tap_changer: Optional[TapChanger] = TapChanger()
