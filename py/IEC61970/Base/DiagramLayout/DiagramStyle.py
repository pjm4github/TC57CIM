# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:25:23 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DiagramLayout.Diagram import Diagram


class DiagramStyle(IdentifiedObject):
    """
    The diagram style refer to a style used by the originating system for a diagram.
    A diagram style describes information such as schematic, geographic, bus-branch etc.
    """

    def __init__(self) -> None:
        super().__init__()
        self.diagram: Diagram = Diagram()

