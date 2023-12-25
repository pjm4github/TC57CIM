# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.SwitchingAction import SwitchingAction
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ACLineSegment import ACLineSegment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Ground import Ground


class GroundAction(SwitchingAction):
    
    def __init__(self):
        super().__init__()
        self.kind = None  # Switching action to perform
        self.grounded_equipment = ConductingEquipment()  # Equipment being grounded with this operation
        self.ground = Ground()  # Ground on which this action is taken
        self.along_ac_line_segment = ACLineSegment()  # The line segment that this ground action will affect (if needed)
