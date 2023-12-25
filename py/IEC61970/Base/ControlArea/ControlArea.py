# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:02:59 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ControlArea.ControlAreaGeneratingUnit import ControlAreaGeneratingUnit
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ControlArea.ControlAreaTypeKind import ControlAreaTypeKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ControlArea.TieFlow import TieFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.LoadModel.EnergyArea import EnergyArea


class ControlArea(PowerSystemResource):
    """
    A control area is a grouping of generating units and/or loads and a cutset of
    tie lines (as terminals) which may be used for a variety of purposes including
    automatic generation control, powerflow solution area interchange control
    specification, and input to load forecasting.  Note that any number of
    overlapping control area specifications can be superimposed on the physical
    model.
    @author: kdd
    @version: 1.0
    @created: 15-Dec-2023 4:38:26 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.net_interchange: Optional[ActivePower] = ActivePower()  # The specified positive net interchange into the control area, i.e. positive sign means flow in to the area
        self.p_tolerance: Optional[ActivePower] = ActivePower()  # Active power net interchange tolerance
        self.type: Optional[ControlAreaTypeKind] = ControlAreaTypeKind.AGC  # The primary type of control area definition used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.  A control area specified with primary type of automatic generation control could still be forecast and used as an interchange area in power flow analysis.
        self.energy_area: Optional[EnergyArea] = EnergyArea()  # The energy area that is forecast from this control area specification
        self.control_area_generating_unit: Optional[ControlAreaGeneratingUnit] = ControlAreaGeneratingUnit()  # The generating unit specificaitons for the control area.
        self.tie_flow: Optional[TieFlow] = TieFlow()  # The tie flows associated with the control area.

