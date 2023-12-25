# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:02:27 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Contingency.ContingencyElement import ContingencyElement
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Contingency.ContingencyEquipmentStatusKind import ContingencyEquipmentStatusKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment

class ContingencyEquipment(ContingencyElement):
    """
    A equipment to which the in service status is to change such as a power
    transformer or AC line segment.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        super().__init__()
        # The status for the associated equipment when in the contingency state.
        #     This status is independent of the case to which the contingency is originally applied,
        #     but defines the equipment status when the contingency is applied.
        self.contingent_status: ContingencyEquipmentStatusKind = ContingencyEquipmentStatusKind.OUT_OF_SERVICE
        self.equipment: Equipment = Equipment()

