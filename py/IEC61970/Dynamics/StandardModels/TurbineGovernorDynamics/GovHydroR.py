# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroR(TurbineGovernorDynamics):
    """
    Fourth order lead-lag governor and hydro turbine.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self):
        super().__init__()
        self.at = PU(1.2)  # Turbine gain (At).  Typical Value = 1.2.
        self.db1 = Frequency(0)  # Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
        self.db2 = ActivePower(0)  # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
        self.dturb = PU(.2)  # Turbine damping factor (Dturb).  Typical Value = 0.2.
        self.eps = Frequency(0)  # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
        self.gmax = PU(1.05)  # Maximum governor output (Gmax).  Typical Value = 1.05.
        self.gmin = PU(-1.05)  # Minimum governor output (Gmin).  Typical Value = -0.05.
        self.gv1 = PU(0)  # Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
        self.gv2 = PU(0)  # Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
        self.gv3 = PU(0)  # Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
        self.gv4 = PU(0)  # Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
        self.gv5 = PU(0)  # Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
        self.gv6 = PU(0)  # Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
        self.h0 = PU(1)  # Turbine nominal head (H0).  Typical Value = 1.
        self.input_signal: bool = False  # Input signal switch (Flag). true = Pe input is used false = feedback is received from CV. Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to true.  Typical Value = true.
        self.kg = PU(2)  # Gate servo gain (Kg).  Typical Value = 2.
        self.ki = PU(.5)  # Integral gain (Ki).  Typical Value = 0.5.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (>0).  Unit = MW.
        self.pgv1 = PU(0)  # Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
        self.pgv2 = PU(0)  # Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
        self.pgv3 = PU(0)  # Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
        self.pgv4 = PU(0)  # Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
        self.pgv5 = PU(0)  # Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
        self.pgv6 = PU(0)  # Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
        self.pmax = PU(1)  # Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1.
        self.pmin = PU(0)  # Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0.
        self.qnl = PU(.08)  # No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08.
        self.r = PU(.05)  # Steady-state droop (R).  Typical Value = 0.05.
        self.t1 = Seconds(1.5)  # Lead time constant 1 (T1).  Typical Value = 1.5.
        self.t2 = Seconds(.1)  # Lag time constant 1 (T2).  Typical Value = 0.1.
        self.t3 = Seconds(1.5)  # Lead time constant 2 (T3).  Typical Value = 1.5.
        self.t4 = Seconds(.1)  # Lag time constant 2 (T4).  Typical Value = 0.1.
        self.t5 = Seconds(0)  # Lead time constant 3 (T5).  Typical Value = 0.
        self.t6 = Seconds(.05)  # Lag time constant 3 (T6).  Typical Value = 0.05.
        self.t7 = Seconds(0)  # Lead time constant 4 (T7).  Typical Value = 0.
        self.t8 = Seconds(.05)  # Lag time constant 4 (T8).  Typical Value = 0.05.
        self.td = Seconds(.05)  # Input filter time constant (Td).  Typical Value = 0.05.
        self.tp = Seconds(.05)  # Gate servo time constant (Tp).  Typical Value = 0.05.
        self.tt = Seconds(0)  # Power feedback time constant (Tt).  Typical Value = 0.
        self.tw = Seconds(1)  # Water inertia time constant (Tw).  Typical Value = 1.
        self.velcl: float = -.2   # Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2.
        self.velop: float = .2   # Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.2.
