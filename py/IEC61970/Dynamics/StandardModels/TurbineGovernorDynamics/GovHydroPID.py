# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPid(TurbineGovernorDynamics):
    """
    PID governor and turbine.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.aturb = PU(-1)  # Turbine numerator multiplier (Aturb) (note 3).  Typical Value -1.
        self.bturb = PU(.5)  # Turbine denominator multiplier (Bturb) (note 3).  Typical Value = 0.5.
        self.db1 = Frequency(0)  # Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
        self.db2 = ActivePower(0)  # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
        self.eps = Frequency(0)  # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
        self.gv1 = PU(0)  # Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
        self.gv2 = PU(0)  # Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
        self.gv3 = PU(0)  # Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
        self.gv4 = PU(0)  # Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
        self.gv5 = PU(0)  # Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
        self.gv6 = PU(0)  # Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
        self.input_signal: bool = True  # Input signal switch (Flag). true = Pe input is used false = feedback is received from CV. Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to true.  Typical Value = true.
        self.kd = PU(1.11)  # Derivative gain (Kd).  Typical Value = 1.11.
        self.kg = PU(2.5)  # Gate servo gain (Kg).  Typical Value = 2.5.
        self.ki = PU(0.36)  # Integral gain (Ki).  Typical Value = 0.36.
        self.kp = PU(0.1)  # Proportional gain (Kp).  Typical Value = 0.1.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (>0).  Unit = MW.
        self.pgv1 = PU(0)  # Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
        self.pgv2 = PU(0)  # Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
        self.pgv3 = PU(0)  # Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
        self.pgv4 = PU(0)  # Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
        self.pgv5 = PU(0)  # Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
        self.pgv6 = PU(0)  # Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
        self.pmax = PU(1)  # Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1.
        self.pmin = PU(0)  # Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0.
        self.r = PU(0.05)  # Steady state droop (R).  Typical Value = 0.05.
        self.td = Seconds(0)  # Input filter time constant (Td).  Typical Value = 0.
        self.tf = Seconds(.1)  # Washout time constant (Tf).  Typical Value = 0.1.
        self.tp = Seconds(.35)  # Gate servo time constant (Tp).  Typical Value = 0.35.
        self.tt = Seconds(0.02)  # Power feedback time constant (Tt).  Typical Value = 0.02.
        self.tturb = Seconds(0.8)  # Turbine time constant (Tturb) (note 3).  Typical Value = 0.8.
        self.velcl: float = -.14  # Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.14.
        self.velop: float = 0.09  #Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.09.
