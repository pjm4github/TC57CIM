# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:02:02 2023
from typing import Any, Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import \
    PFVarControllerType1Dynamics


class PfVarType1IeeeVarController(PFVarControllerType1Dynamics):
    """
    The class represents IEEE VAR Controller Type 1 which operates by moving the
    voltage reference directly.
    
    Reference: IEEE Standard 421.5-2005 Section 11.3.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
        """
        Var controller time delay (<i>T</i><i><sub>VARC</sub></i>).  Type: Seconds = Seconds()
        Typical Value = 5.
        """
        self.tvarc: Seconds = Seconds(5.0)
        
        """
        Synchronous machine power factor (<i>V</i><i><sub>VAR</sub></i>).  Type: PU = PU()
        """
        self.vvar: PU = PU()
        
        """
        Var controller dead band (<i>V</i><i><sub>VARC_BW</sub></i>).  Type: Float
        Typical Value = 0.02.
        """
        self.vvarcbw: float = 0.2
        
        """
        Var controller reference (<i>V</i><i><sub>VARREF</sub></i>).  Type: PU = PU()
        """
        self.vvarref: PU = PU()
        
        """
        Maximum machine terminal voltage needed for pf/var controller to be enabled
        (<i>V</i><i><sub>VTMAX</sub></i>).  Type: PU = PU()
        """
        self.vvtmax: PU = PU()
        
        """
        Minimum machine terminal voltage needed to enable pf/var controller
        (<i>V</i><i><sub>VTMIN</sub></i>).  Type: PU = PU()
        """
        self.vvtmin: PU = PU()
