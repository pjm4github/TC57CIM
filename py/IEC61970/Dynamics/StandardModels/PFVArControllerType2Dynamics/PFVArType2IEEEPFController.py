# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:02:30 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.PFVArControllerType2Dynamics.PFVArControllerType2Dynamics import \
    PFVArControllerType2Dynamics


class PfVarType2IeeePfController(PFVArControllerType2Dynamics):
    """ 
    The class represents IEEE PF Controller Type 2 which is a summing 
    point type controller and makes up the outside loop of a two-loop system. 
    This controller is implemented as a slow PI type controller. The voltage 
    regulator forms the inner loop and is implemented as a fast controller. 

    Reference: IEEE Standard 421.5-2005 Section 11.4. 
    @author: pcha006 
    @version: 1.0 
    @created: 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.exlon: bool = True  # Overexcitation or under excitation flag (EXLON)
        self.ki: PU = PU()  # Integral gain of the pf controller (K<I>I)
        self.kp: PU = PU()  # Proportional gain of the pf controller (K<P>p)
        self.pfref: PU = PU()  # Power factor reference (P<F>REF)
        self.vclmt: PU = PU()  # Maximum output of the pf controller (V<CLMT>)
        self.vref: PU = PU()  # Voltage regulator reference (V<REF>)
        self.vs: float = 0.0  # Generator sensing voltage (V<S>)
