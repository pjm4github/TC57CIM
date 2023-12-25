# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ACDCTerminal import ACDCTerminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCTopologicalNode import DCTopologicalNode


class DCBaseTerminal(ACDCTerminal):
    """
    An electrical connection point at a piece of DC conducting equipment. DC
    terminals are connected at one physical DC node that may have multiple DC
    terminals connected. A DC node is similar to an AC connectivity node. The
    model enforces that DC connections are distinct from AC connections.
    @author selaost1
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """

    def __init__(self) -> None:

        # See association end Terminal.TopologicalNode.
        super().__init__()
        self.dc_topological_node = DCTopologicalNode()

