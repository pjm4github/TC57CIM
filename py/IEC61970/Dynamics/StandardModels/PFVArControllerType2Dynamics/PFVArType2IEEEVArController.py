# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:02:30 2023
from typing import Optional, Union

from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.PFVArControllerType2Dynamics.PFVArControllerType2Dynamics import \
    PFVArControllerType2Dynamics


class PFVarType2IEEEVarController(PFVArControllerType2Dynamics):
    """
    The class represents IEEE VAR Controller Type 2 which is a summing point type
    controller. It makes up the outside loop of a two-loop system. This controller
    is implemented as a slow PI type controller, and the voltage regulator forms
    the inner loop and is implemented as a fast controller.

    Reference: IEEE Standard 421.5-2005 Section 11.5.
    """

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        self.exlon: Optional[bool] = False  # Overexcitation or under excitation flag (EXLON)
        self.ki: PU = PU(0.0)  # Integral gain of the pf controller (K_I)
        self.kp: PU = PU(0.0)  # Proportional gain of the pf controller (K_P)
        self.q_ref: PU = PU(0.0)  # Reactive power reference (Q_REF)
        self.v_clmt: PU = PU(0.0)  # Maximum output of the pf controller (V_CLMT)
        self.v_ref: PU = PU(0.0)  # Voltage regulator reference (V_REF)
        self.vs: Optional[float] = 0.0  # Generator sensing voltage (V_S)
