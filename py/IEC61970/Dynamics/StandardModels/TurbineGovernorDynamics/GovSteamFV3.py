from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics import TurbineGovernorDynamics

class GovSteamFV3(TurbineGovernorDynamics):
    """
    Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast valving.
    """
    def __init__(self):
        super().__init__()
        self.k = PU(20)  # Governor gain, (reciprocal of droop) (K).  Typical Value = 20.
        self.k1 = PU(0.2)  # Fraction of turbine power developed after first boiler pass (K1).  Typical Value = 0.2.
        self.k2 = PU(0.2)  # Fraction of turbine power developed after second boiler pass (K2).  Typical Value = 0.2.
        self.k3 = PU(0.6)  # Fraction of hp turbine power developed after crossover or third boiler pass (K3). Typical Value = 0.6.
        self.mwbase = ActivePower()  # Base for power values (MWbase) (>0).  Unit = MW.
        self.pmax = PU(1)  # Maximum valve opening, PU of MWbase (Pmax).  Typical Value = 1.
        self.pmin = PU(0)  # Minimum valve opening, PU of MWbase (Pmin).  Typical Value = 0.
        self.prmax = PU(1)  # Max. pressure in reheater (Prmax).  Typical Value = 1.
        self.t1 = Seconds(0)  # Governor lead time constant (T1).  Typical Value = 0.
        self.t2 = Seconds(0)  # Governor lag time constant (T2).  Typical Value = 0.
        self.t3 = Seconds(0)  # Valve positioner time constant (T3).  Typical Value = 0.
        self.t4 = Seconds(0.2)  # Inlet piping/steam bowl time constant (T4).  Typical Value = 0.2.
        self.t5 = Seconds(0.5)  # Time constant of second boiler pass (i.e. reheater) (T5).  Typical Value = 0.5.
        self.t6 = Seconds(10)  # Time constant of crossover or third boiler pass (T6).  Typical Value = 10.
        self.ta = Seconds(0.97)  # Time to close intercept valve (IV) (Ta).  Typical Value = 0.97.
        self.tb = Seconds(0.98)  # Time until IV starts to reopen (Tb).  Typical Value = 0.98.
        self.tc = Seconds(0.99)  # Time until IV is fully open (Tc).  Typical Value = 0.99.
        self.uc = -1  # Maximum valve closing velocity (Uc).  Unit = PU/sec.  Typical Value = -1.
        self.uo = 0.1  # Maximum valve opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1.
