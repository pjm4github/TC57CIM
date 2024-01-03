from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamCC(TurbineGovernorDynamics):
    """
    Cross compound turbine governor model.
    """
    def __init__(self):
        super().__init__()
        self.dhp = PU(0)  # HP damping factor (Dhp).  Typical Value = 0.
        self.dlp = PU(0)  # LP damping factor (Dlp).  Typical Value = 0.
        self.fhp = PU(0.3)  # Fraction of HP power ahead of reheater (Fhp).  Typical Value = 0.3.
        self.flp = PU(0.7)  # Fraction of LP power ahead of reheater (Flp).  Typical Value = 0.7.
        self.mwbase = ActivePower()  # Base for power values (MWbase) (>0).  Unit = MW.
        self.pmaxhp = PU(1)  # Maximum HP value position (Pmaxhp).  Typical Value = 1.
        self.pmaxlp = PU(1)  # Maximum LP value position (Pmaxlp).  Typical Value = 1.
        self.rhp = PU(0.05)  # HP governor droop (Rhp).  Typical Value = 0.05.
        self.rlp = PU(0.05)  # LP governor droop (Rlp).  Typical Value = 0.05.
        self.t1hp = Seconds(0.1)  # HP governor time constant (T1hp).  Typical Value = 0.1.
        self.t1lp = Seconds(0.1)  # LP governor time constant (T1lp).  Typical Value = 0.1.
        self.t3hp = Seconds(0.1)  # HP turbine time constant (T3hp).  Typical Value = 0.1.
        self.t3lp = Seconds(0.1)  # LP turbine time constant (T3lp).  Typical Value = 0.1.
        self.t4hp = Seconds(0.1)  # HP turbine time constant (T4hp).  Typical Value = 0.1.
        self.t4lp = Seconds(0.1)  # LP turbine time constant (T4lp).  Typical Value = 0.1.
        self.t5hp = Seconds(10)  # HP reheater time constant (T5hp).  Typical Value = 10.
        self.t5lp = Seconds(10)  # LP reheater time constant (T5lp).  Typical Value = 10.
