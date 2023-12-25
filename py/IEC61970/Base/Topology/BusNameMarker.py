# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:41:40 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ACDCTerminal import ACDCTerminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ReportingGroup import ReportingGroup
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Topology.TopologicalNode import TopologicalNode


class BusNameMarker(IdentifiedObject):
    """
    Used to apply user standard names to topology buses. Typically used for "bus/branch" case generation.
    Associated with one or more terminals that are normally connected with the bus name.
    The associated terminals are normally connected by non-retained switches.
    For a ring bus station configuration, all busbar terminals in the ring are typically associated.
    For a breaker and a half scheme, both busbars would normally be associated.
    For a ring bus, all busbars would normally be associated.
    For a "straight" busbar configuration, normally only the main terminal at the busbar would be associated.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """



    def __init__(self):
        super().__init__()
        self.priority: int = 0
        self.reporting_group: ReportingGroup = ReportingGroup()
        self.terminal: ACDCTerminal = ACDCTerminal()
        self.topological_node: TopologicalNode = TopologicalNode()
