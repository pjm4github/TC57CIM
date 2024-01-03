# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:25:38 2023
from typing import Any, Generic, TypeVar

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """
    The class represents the Type UEL1 model which has a circular limit boundary
    when plotted in terms of machine reactive power vs. real power output.

    Reference: IEEE UEL1 421.5-2005 Section 10.1.
    """

    def __init__(self, kuc=1.38, kuf=3.3, kui=0, kul=100, kur=1.95, tu1=0, tu2=0.05, tu3=0, tu4=0, vucmax=5.8, vuimax=None, vuimin=None, vulmax=18, vulmin=-18, vurmax=5.8):
        super().__init__()
        self.kuc = PU(kuc)  # UEL center setting (K_UC)
        self.kuf = PU(kuf)  # UEL excitation system stabilizer gain (K_UF)
        self.kui = PU(kui)  # UEL integral gain (K_UI)
        self.kul = PU(kul)  # UEL proportional gain (K_UL)
        self.kur = PU(kur)  # UEL radius setting (K_UR)
        self.tu1 = Seconds(tu1)  # UEL lead time constant (T_U1)
        self.tu2 = Seconds(tu2)  # UEL lag time constant (T_U2)
        self.tu3 = Seconds(tu3)  # UEL lead time constant (T_U3)
        self.tu4 = Seconds(tu4)  # UEL lag time constant (T_U4)
        self.vucmax = PU(vucmax)  # UEL maximum limit for operating point phasor magnitude (V_UCMAX)
        self.vuimax = PU(vuimax)  # UEL integrator output maximum limit (V_UIMAX)
        self.vuimin = PU(vuimin)  # UEL integrator output minimum limit (V_UIMIN)
        self.vulmax = PU(vulmax)  # UEL output maximum limit (V_ULMAX)
        self.vulmin = PU(vulmin)  # UEL output minimum limit (V_ULMIN)
        self.vurmax = PU(vurmax)  # UEL maximum limit for radius phasor magnitude (V_URMAX)
