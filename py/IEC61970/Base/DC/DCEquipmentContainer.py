# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.EquipmentContainer import EquipmentContainer
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCTopologicalNode import DCTopologicalNode

class DCEquipmentContainer(EquipmentContainer):
    """
    A modeling construct to provide a root class for containment of DC as well as
    AC equipment. The class differs from the EquipmentContaner for AC in that
    it may also contain DCNodes. Hence it can contain both AC and DC equipment.
    """
    def __init__(self) -> None:
        super().__init__()


