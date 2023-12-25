# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.SwitchingAction import SwitchingAction
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.TempEquipActionKind import TempEquipActionKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ACLineSegment import ACLineSegment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Jumper import Jumper


class JumperAction(SwitchingAction):

    def __init__(self):
        super().__init__()
        self.kind = TempEquipActionKind()
        self.jumper = Jumper()
        self.along_ac_line_segments = ACLineSegment()
        self.jumped_equipments = ConductingEquipment()
