# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:41:01 2023
from typing import Optional
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.StateVariable import StateVariable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ShuntCompensator import ShuntCompensator


class SvShuntCompensatorSections(StateVariable):
    """
    State variable for the number of sections in service for a shunt compensator.
    @author: kdd
    @version: 1.0
    @created: 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.sections: Optional[float] = 1.0  # The number of sections in service as a continuous variable. To get integer value, scale with ShuntCompensator.b_per_section.
        self.shunt_compensator: Optional[ShuntCompensator] = ShuntCompensator()  # The shunt compensator for which the state applies.
