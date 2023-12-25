from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCTopologicalNode import DCTopologicalNode


class DCTopologicalIsland(IdentifiedObject):

    """
    An electrically connected subset of the network. DC
    topological islands can change as the current network
    state changes: e.g. due to
    - disconnect switches or breakers change state in a SCADA/EMS
    - manual creation, change or deletion of topological nodes in a planning tool.
    @author SELAOST1
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """

    def __init__(self) -> None:
        """
        The DC topological nodes in a DC topological island.
        """
        super().__init__()
        self.DCTopologicalNodes: DCTopologicalNode = DCTopologicalNode()

