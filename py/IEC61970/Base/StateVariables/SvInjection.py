# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:41:01 2023

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.StateVariable import StateVariable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.SvVoltage import SinglePhaseKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Topology.TopologicalNode import TopologicalNode


class SvInjection(StateVariable):
    """
    The SvInjection is reporting the calculated bus injection minus the sum of the terminal flows. The terminal flow
    is positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection may
    have the remainder after state estimation or slack after power flow calculation.

    @author: kdd
    @version: 1.0
    @created: 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.phase: SinglePhaseKind = SinglePhaseKind.A
        self.p_injection: ActivePower = ActivePower()
        self.q_injection: ReactivePower = ReactivePower()
        self.topological_node: TopologicalNode = TopologicalNode()
