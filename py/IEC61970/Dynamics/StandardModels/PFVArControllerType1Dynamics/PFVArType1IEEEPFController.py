# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:02:02 2023

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import \
    PFVArControllerType1Dynamics


class PFVarType1IeeePFController(PFVArControllerType1Dynamics):
    """
    The class represents IEEE PF Controller Type 1 which operates by moving the
    voltage reference directly. Reference: IEEE Standard 421.5-2005 Section 11.2.
    """

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        self.ovex: bool = False  # Overexcitation Flag (OVEX)
        self.tpfc: Seconds = Seconds(5.0)  # PF controller time delay (T_PFC)
        self.vitmin: PU = PU()  # Minimum machine terminal current needed to enable pf/var controller (V_ITMIN)
        self.vpf: PU = PU()  # Synchronous machine power factor (V_PF)
        self.vpfcbw: float = 0.0  # PF controller dead band (V_PFC_BW)
        self.vpfref: PU = PU()  # PF controller reference (V_PFREF)
        self.vvtmax: PU = PU()  # Maximum machine terminal voltage needed for pf/var controller to be enabled (V_TMAX)
        self.vvtmin: PU = PU()  # Minimum machine terminal voltage needed to enable pf/var controller (V_TMIN)
