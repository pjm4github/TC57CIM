# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:25:23 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DiagramLayout.OrientationKind import OrientationKind


class Diagram(IdentifiedObject):
    """
    The diagram being exchanged.  The coordinate system is a standard Cartesian
    coordinate system and the orientation attribute defines the orientation.
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.orientation: OrientationKind = OrientationKind.NEGATIVE
        self.x1_initial_view: float = 0.0
        self.x2_initial_view: float = 0.0
        self.y1_initial_view: float = 0.0
        self.y2_initial_view: float = 0.0

