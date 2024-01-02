# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Union

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydro3(TurbineGovernorDynamics):
    """
    Modified IEEE Hydro Governor-Turbine Model. 
    
    This model differs from that defined in the IEEE modeling guideline paper in
    that the limits on gate position and velocity do not permit "wind up" of the
    upstream signals.
    
    @author: tsaxton
    @version: 1.0
    @created: 29-Dec-2023 11:24:18 PM
    """
    
    def __init__(self) -> None:
        """
        Constructor for GovHydro3
        """
        super().__init__()
        self.at = PU(1.2)  # Turbine gain (At).  Typical Value = 1.2.
        self.db1 = Frequency(0)  # Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
        self.db2 = ActivePower(0)  # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
        self.dturb = PU(.2)  # Turbine damping factor (Dturb).  Typical Value = 0.2.
        self.eps = Frequency(0)  # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
        self.governor_control: bool = True  # Governor control flag (Cflag).
        # true = PID control is active false = double derivative control is active. Typical Value = true.
        self.gv1 = PU(0)  # Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
        self.gv2 = PU(0)  # Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
        self.gv3 = PU(0)  # Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
        self.gv4 = PU(0)  # Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
        self.gv5 = PU(0)  # Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
        self.gv6 = PU(0)  # Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
        self.h0 = PU(1)  # Turbine nominal head (H0).  Typical Value = 1.
        self.k1 = PU(.01)  # Derivative gain (K1).  Typical Value = 0.01.
        self.k2 = PU(2.5)  # Double derivative gain, if Cflag = -1 (K2).  Typical Value = 2.5.
        self.kg = PU(2)  # Gate servo gain (Kg).  Typical Value = 2.
        self.ki = PU(.5)  # Integral gain (Ki).  Typical Value = 0.5.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (> 0).  Unit = MW.
        self.pgv1 = PU(0)  # Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
        self.pgv2 = PU(0)  # Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
        self.pgv3 = PU(0)  # Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
        self.pgv4 = PU(0)  # Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
        self.pgv5 = PU(0)  # Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
        self.pgv6 = PU(0)  # Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
        self.pmax = PU(1)  # Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1.
        self.pmin = PU(0)  # Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0.
        self.qnl = PU(.08)  # No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08.
        self.relec = PU(.05)  # Steady-state droop, PU, for electrical power feedback (Relec).  Typical Value = 0.05.
        self.rgate = PU(0)  # Steady-state droop, PU, for governor output feedback (Rgate).  Typical Value = 0.
        self.td = Seconds(.05)  # Input filter time constant (Td).  Typical Value = 0.05.
        self.tf = Seconds(.1)  # Washout time constant (Tf).  Typical Value = 0.1.
        self.tp = Seconds(.05)  # Gate servo time constant (Tp).  Typical Value = 0.05.
        self.tt = Seconds(.2)  # Power feedback time constant (Tt).  Typical Value = 0.2.
        self.tw = Seconds(1)  # Water inertia time constant (Tw).  Typical Value = 1.
        self.velcl: float = -0.2  # Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2.
        self.velop: float = 0.2  # Maximum gate opening velocity (Velop).  Unit = PU/sec. Typical Value = 0.2.
