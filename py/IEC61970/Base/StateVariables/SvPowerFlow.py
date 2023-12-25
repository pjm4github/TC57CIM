# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:41:01 2023
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.StateVariable import StateVariable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.SvVoltage import SinglePhaseKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.InfIEC61970.EnergyArea.EnergyGroup import EnergyGroup


# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.state_variable import StateVariable
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Curve import ActivePower, ReactivePower
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Wires.PhaseCode import SinglePhaseKind
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Meas.EnergyValues import EnergyGroup



class SvPowerFlow(StateVariable):
    """
    State variable for power flow. Load convention is used for flow direction. This 
    means flow out from the TopologicalNode into the equipment is positive.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.p: ActivePower = ActivePower()
        self.phase: SinglePhaseKind = SinglePhaseKind.A
        self.q: ReactivePower = ReactivePower()
        self.terminal: Terminal = Terminal()
        self.energy_group: EnergyGroup = EnergyGroup()

