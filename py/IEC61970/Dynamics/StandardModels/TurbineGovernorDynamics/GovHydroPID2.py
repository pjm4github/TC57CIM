# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Optional, Any, Union

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPid2(TurbineGovernorDynamics):
    def __init__(self) -> None:

        super().__init__()
        self.atw: PU = PU(0)  # Factor multiplying Tw (Atw).  Typical Value = 0.
        self.d: PU = PU(0)  # Turbine damping factor (D).  Unit = delta P / delta speed.  Typical Value = 0.
        # Feedback signal type flag (Flag).
        # True = use gate position feedback signal
        # False = use Pe.
        self.feedback_signal: bool  = False
        self.g0: PU = PU(0)  # Gate opening at speed no load (G0).  Typical Value = 0.
        self.g1: PU = PU(0)  # Intermediate gate opening (G1).  Typical Value = 0.
        self.g2: PU = PU(0)   # Intermediate gate opening (G2).  Typical Value = 0.
        self.gmax: PU = PU(0)  # Maximum gate opening (Gmax).  Typical Value = 0.
        self.gmin: PU = PU(0)  # Minimum gate opening (Gmin).  Typical Value = 0.
        self.kd: PU = PU(0)  # Derivative gain (Kd).  Typical Value = 0.
        self.ki: float = 0.0  # Reset gain (Ki).  Unit = PU/sec.  Typical Value = 0.
        self.kp: PU = PU(0)  # Proportional gain (Kp).  Typical Value = 0.
        self.mwbase: Optional[ActivePower] = ActivePower(.1)  # Base for power values (MWbase) (>0).  Unit = MW.  Typical Value = 0.
        self.p1: PU = PU(0)  # Power at gate opening G1 (P1).  Typical Value = 0.
        self.p2: PU = PU(0)  # Power at gate opening G2 (P2).  Typical Value = 0.
        self.p3: PU = PU(0)  # Power at full opened gate (P3).  Typical Value = 0.
        self.rperm: PU = PU(0)  # Permanent drop (Rperm).  Typical Value = 0.
        self.ta: Seconds = Seconds(0)  # Controller time constant (Ta) (>0).  Typical Value = 0.
        self.tb: Seconds = Seconds(0)  # Gate servo time constant (Tb) (>0).  Typical Value = 0.
        self.treg: Seconds = Seconds(0)  # Speed detector time constant (Treg).  Typical Value = 0.
        self.tw: Seconds = Seconds(0)  # Water inertia time constant (Tw) (>0).  Typical Value = 0.
        self.velmax: float = 0.0  # Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0.
        self.velmin: float = 0.0  # Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0.
