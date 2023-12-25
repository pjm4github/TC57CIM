# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCBaseTerminal import DCBaseTerminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCEquipmentContainer import DCEquipmentContainer
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCTopologicalNode import DCTopologicalNode


class DCNode(IdentifiedObject):
    """
    DC nodes are points where terminals of DC conducting equipment are connected
    together with zero impedance.
    @author SELAOST1
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.DCTerminals: DCBaseTerminal = DCBaseTerminal()
        self.DCTopologicalNode: DCTopologicalNode = DCTopologicalNode()
        self.DCEquipmentContainer: DCEquipmentContainer = DCEquipmentContainer()
