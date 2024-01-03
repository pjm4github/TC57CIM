# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamSGO(TurbineGovernorDynamics):
    """
    Simplified Steam turbine governor model.
    """

    def __init__(self):
        super().__init__()
        self.k1 = PU()  # One/per unit regulation (K1)
        self.k2 = PU()  # Fraction (K2)
        self.k3 = PU()  # Fraction (K3)
        self.mwbase = ActivePower()  # Base for power values (MWbase) (>0). Unit = MW
        self.pmax = PU()  # Upper power limit (Pmax)
        self.pmin = Seconds()  # Lower power limit (Pmin)
        self.t1 = Seconds()  # Controller lag (T1)
        self.t2 = Seconds()  # Controller lead compensation (T2)
        self.t3 = Seconds()  # Governor lag (T3) (>0)
        self.t4 = Seconds()  # Delay due to steam inlet volumes associated with steam chest and inlet piping (T4)
        self.t5 = Seconds()  # Reheater delay including hot and cold leads (T5)
        self.t6 = Seconds()  # Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6)
