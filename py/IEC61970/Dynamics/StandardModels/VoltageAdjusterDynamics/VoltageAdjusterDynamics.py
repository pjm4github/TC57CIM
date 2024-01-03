# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:26:32 2023
from datetime import datetime
from typing import Optional

from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import \
    PFVarControllerType1Dynamics


class VoltageAdjusterDynamics(DynamicsFunctionBlock):
    """
    Voltage adjuster function block whose behaviour is described by reference to a
    standard model or by definition of a user-defined model.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        # Power Factor or VAr controller Type I model with which this voltage adjuster is associated.
        self.pf_var_controller_type1_dynamics: PFVarControllerType1Dynamics = PFVarControllerType1Dynamics()
