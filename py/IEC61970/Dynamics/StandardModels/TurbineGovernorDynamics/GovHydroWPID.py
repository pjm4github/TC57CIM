# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroWPID(TurbineGovernorDynamics):
    """
    Woodward PID Hydro Governor.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.d: PU = PU()  # Turbine damping factor (D).  Unit = delta P / delta speed.
        self.gatmax: PU = PU()  # Gate opening Limit Maximum (Gatmax).
        self.gatmin: PU = PU()  # Gate opening Limit Minimum (Gatmin).
        self.gv1: PU = PU()  # Gate position 1 (Gv1).
        self.gv2: PU = PU()  # Gate position 2 (Gv2).
        self.gv3: PU = PU()  # Gate position 3 (Gv3).
        self.kd: PU = PU()  # Derivative gain (Kd).  Typical Value = 1.11.
        self.ki: PU = PU()  # Reset gain (Ki).  Typical Value = 0.36.
        self.kp: PU = PU()  # Proportional gain (Kp).  Typical Value = 0.1.
        self.mwbase: Optional[ActivePower] = ActivePower()  # Base for power values  (MWbase) (>0).  Unit = MW.
        self.pgv1: PU = PU()  # Output at Gv1 PU of MWbase (Pgv1).
        self.pgv2: PU = PU()  # Output at Gv2 PU of MWbase (Pgv2).
        self.pgv3: PU = PU()  # Output at Gv3 PU of MWbase (Pgv3).
        self.pmax: PU = PU()  # Maximum Power Output (Pmax).
        self.pmin: PU = PU()  # Minimum Power Output (Pmin).
        self.reg: PU = PU()  # Permanent drop (Reg).
        self.ta: Seconds = Seconds()  # Controller time constant (Ta) (>0).  Typical Value = 0.
        self.tb: Seconds = Seconds()  # Gate servo time constant (Tb) (>0).  Typical Value = 0.
        self.treg: Seconds = Seconds()  # Speed detector time constant (Treg).
        self.tw: Seconds = Seconds()  # Water inertia time constant (Tw) (>0).  Typical Value = 0.
        self.velmax: PU = PU()  # Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0.
        self.velmin: PU = PU()  # Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0.
