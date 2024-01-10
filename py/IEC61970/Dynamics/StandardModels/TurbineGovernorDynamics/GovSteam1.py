# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam1(TurbineGovernorDynamics):
    """
    Steam turbine governor model, based on the GovSteamIEEE1 model  (with optional
    deadband and nonlinear valve gain added).
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """
    def __init__(self):
        super().__init__()
        self.db1 = Frequency(0)  # Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
        self.db2 = ActivePower(0)  # Unintentional deadband (db2).  Unit = MW.  Typical Value = 0.
        self.eps = Frequency(0)  # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
        self.gv1 = PU(0)  # Nonlinear gain valve position point 1 (GV1).  Typical Value = 0.
        self.gv2 = PU(.4)  # Nonlinear gain valve position point 2 (GV2).  Typical Value = 0.4.
        self.gv3 = PU(.5)  # Nonlinear gain valve position point 3 (GV3).  Typical Value = 0.5.
        self.gv4 = PU(.6)  # Nonlinear gain valve position point 4 (GV4).  Typical Value = 0.6.
        self.gv5 = PU(1)  # Nonlinear gain valve position point 5 (GV5).  Typical Value = 1.
        self.gv6 = PU(0)  # Nonlinear gain valve position point 6 (GV6).  Typical Value = 0.
        self.k = PU(25)  # Governor gain (reciprocal of droop) (K) (>0).  Typical Value = 25.
        self.k1 = 0.2  # Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2.
        self.k2 = 0.  # Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0.
        self.k3 = 0.3  # Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3.
        self.k4 = 0.  # Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0.
        self.k5 = 0.5  # Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5.
        self.k6 = 0.  # Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0.
        self.k7 = 0.  # Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0.
        self.k8 = 0.  # Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (>0).  Unit = MW.
        self.pgv1 = PU(0)  # Nonlinear gain power value point 1 (Pgv1).  Typical Value = 0.
        self.pgv2 = PU(.75)  # Nonlinear gain power value point 2 (Pgv2).  Typical Value = 0.75.
        self.pgv3 = PU(.91)  # Nonlinear gain power value point 3 (Pgv3).  Typical Value = 0.91.
        self.pgv4 = PU(.98)  # Nonlinear gain power value point 4 (Pgv4).  Typical Value = 0.98.
        self.pgv5 = PU(1)  # Nonlinear gain power value point 5 (Pgv5).  Typical Value = 1.
        self.pgv6 = PU(0)  # Nonlinear gain power value point 6 (Pgv6).  Typical Value = 0.
        self.pmax = PU(1)  # Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1.
        self.pmin = PU(0)  # Minimum valve opening (Pmin) (>=0).  Typical Value = 0.
        self.sdb1 = True  # Intentional deadband indicator. true = intentional deadband is applied false = intentional deadband is not applied. Typical Value = true.
        self.sdb2 = True  # Unintentional deadband location. true = intentional deadband is applied before point "A" false = intentional deadband is applied after point "A". Typical Value = true.
        self.t1 = Seconds(0)  # Governor lag time constant (T1).  Typical Value = 0.
        self.t2 = Seconds(0)  # Governor lead time constant (T2).  Typical Value = 0.
        self.t3 = Seconds(.1)  # Valve positioner time constant (T3) (>0).  Typical Value = 0.1.
        self.t4 = Seconds(.3)  # Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3.
        self.t5 = Seconds(5)  # Time constant of second boiler pass (T5).  Typical Value = 5.
        self.t6 = Seconds(.5)  # Time constant of third boiler pass (T6).  Typical Value = 0.5.
        self.t7 = Seconds(0)  # Time constant of fourth boiler pass (T7).  Typical Value = 0.
        self.uc = -10.  # Maximum valve closing velocity (Uc) (<0).  Unit = PU/sec.  Typical Value = -10.
        self.uo = 1.  # Maximum valve opening velocity (Uo) (>0).  Unit = PU/sec.  Typical Value = 1.
        self.valve = True  # Nonlinear valve characteristic. true = nonlinear valve characteristic is used false = nonlinear valve characteristic is not used. Typical Value = true.
