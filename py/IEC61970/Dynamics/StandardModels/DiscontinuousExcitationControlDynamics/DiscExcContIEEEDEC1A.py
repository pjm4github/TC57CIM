# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:59:32 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import \
    DiscontinuousExcitationControlDynamics


class DiscExcContIeeeDec1A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC1A discontinuous excitation control model
    that boosts generator excitation to a level higher than that demanded by the
    voltage regulator and stabilizer immediately following a system fault.

    Reference: IEEE Standard 421.5-2005 Section 12.2.
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.esc: PU = PU(.0015)  # Speed change reference (E_SC). Typical Value = 0.0015
        self.kan: PU = PU(400.0)  # Discontinuous controller gain (K_AN). Typical Value = 400.0
        self.ketl: PU = PU(47.0)  # Terminal voltage limiter gain (K_ETL). Typical Value = 47.0
        self.tan: Seconds = Seconds(0.08)  # Discontinuous controller time constant (T_AN). Typical Value = 0.08
        self.td: Seconds = Seconds(0.03)  # Time constant (T_D). Typical Value = 0.03
        self.tl1: Seconds = Seconds(0.025)  # Time constant (T_L1). Typical Value = 0.025
        self.tl2: Seconds = Seconds(1.25)  # Time constant (T_L2). Typical Value = 1.25
        self.tw5: Seconds = Seconds(5.0)  # DEC washout time constant (T_W5). Typical Value = 5.0
        self.val: PU = PU(5.0)  # Regulator voltage reference (V_AL). Typical Value = 5.0
        self.vanmax: PU = PU(0.0)  # Limiter for Van (V_ANMAX)
        self.vomax: PU = PU(1.0)  # Limiter (V_OMAX). Typical Value = 0.3
        self.vomin: PU = PU(1.0)  # Limiter (V_OMIN). Typical Value = 0.1
        self.vsmax: PU = PU(1.0)  # Limiter (V_SMAX). Typical Value = 0.2
        self.vsmin: PU = PU(1.0)  # Limiter (V_SMIN). Typical Value = -0.066
        self.vtc: PU = PU(1.0)  # Terminal voltage level reference (V_TC). Typical Value = 0.95
        self.vtlmt: PU = PU(1.0)  # Voltage reference (V_TLMT). Typical Value = 1.1
        self.vtm: PU = PU(1.0)  # Voltage limits (V_TM). Typical Value = 1.13
        self.vtn: PU = PU(1.0)  # Voltage limits (V_TN). Typical Value = 1.12
