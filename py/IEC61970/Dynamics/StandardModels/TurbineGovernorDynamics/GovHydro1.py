# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Union

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydro1(TurbineGovernorDynamics):
    """
    Basic Hydro turbine governor model.
    @ author tsaxton
    @ version 1.0
    @ created 29-Dec-2023 11:24:18 PM
    """
    def __init__(self):
        super().__init__()
        self.at = PU(1.2)  # Turbine gain (At) (>0).  Typical Value = 1.2.
        self.dturb = PU(0.5)  # Turbine damping factor (Dturb) (>=0).  Typical Value = 0.5.
        self.gmax = PU(1)  # Maximum gate opening (Gmax) (>0).  Typical Value = 1.
        self.gmin = PU(0)  # Minimum gate opening (Gmin) (>=0).  Typical Value = 0.
        self.hdam = PU(1)  # Turbine nominal head (hdam).  Typical Value = 1.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (> 0).  Unit = MW.
        self.qnl = PU(0.08)  # No-load flow at nominal head (qnl) (>=0).  Typical Value = 0.08.
        self.rperm = PU(0.04)  # Permanent droop (R) (>0).  Typical Value = 0.04.
        self.rtemp = PU(.3)  # Temporary droop (r) (>R).  Typical Value = 0.3.
        self.tf = Seconds(0.05)  # Filter time constant (<i>Tf</i>) (>0).  Typical Value = 0.05.
        self.tg = Seconds(0.5)  # Gate servo time constant (Tg) (>0).  Typical Value = 0.5.
        self.tr = Seconds(5)  # Washout time constant (Tr) (>0).  Typical Value = 5.
        self.tw = Seconds(1)  # Water inertia time constant (Tw) (>0).  Typical Value = 1.
        self.velm: float = 0.2  # Maximum gate velocity (Vlem) (>0).  Typical Value = 0.2.
