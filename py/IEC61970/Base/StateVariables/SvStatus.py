# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:41:01 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.StateVariable import StateVariable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.SvVoltage import SinglePhaseKind


# from conducting_equipment import ConductingEquipment
# from state_variable import StateVariable
# from single_phase_kind import SinglePhaseKind


class SvStatus(StateVariable):
    """
    State variable for status.
    
    @author: kdd
    @version: 1.0
    @created: 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.in_service: Optional[bool] = False  # The in service status as a result of topology processing.
        self.phase: Optional[SinglePhaseKind] = SinglePhaseKind.A  # The individual phase status. If the attribute is unspecified, then three phase model is assumed.
        self.conducting_equipment: Optional[ConductingEquipment] = ConductingEquipment()  # The conducting equipment associated with the status state variable.
