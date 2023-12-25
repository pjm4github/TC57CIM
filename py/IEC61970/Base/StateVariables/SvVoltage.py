# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:41:01 2023
from typing import Optional
from enum import Enum

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables import StateVariable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Topology.TopologicalNode import TopologicalNode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind


# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core import AngleDegrees, Voltage, TopologicalNode


class SvVoltage(StateVariable):
    """
    State variable for voltage.

    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        self.angle: Optional[AngleDegrees] = AngleDegrees()  # The voltage angle of the topological node complex voltage with respect to system reference.
        self.phase: Optional[SinglePhaseKind] = SinglePhaseKind.A  # If specified the voltage is the line to ground voltage of the individual phase. If unspecified, then the voltage is assumed balanced.
        self.v: Optional[Voltage] = Voltage()  # The voltage magnitude at the topological node.
        self.topological_node: Optional[TopologicalNode] = TopologicalNode()  # The topological node associated with the voltage state.
