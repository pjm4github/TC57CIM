# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamIEEE1(TurbineGovernorDynamics):
    """
    IEEE steam turbine governor model.

    Reference: IEEE Transactions on Power Apparatus and Systems
    November/December 1973, Volume PAS-92, Number 6
    Dynamic Models for Steam and Hydro Turbines in Power System Studies, Page 1904.

    Parameter Notes:
    - Per unit parameters are on base of MWbase, which is normally the MW capability of the turbine.
    - T3 must be greater than zero. All other time constants may be zero.
    - For a tandem-compound turbine the parameters K2, K4, K6, and K8 are ignored. For a cross-compound turbine, two generators are connected to this turbine-governor model.
    - Each generator must be represented in the load flow by data on its own MVA base. The values of K1, K3, K5, K7 must be specified to describe the proportionate development of power on the first turbine shaft. K2, K4, K6, K8 must describe the second turbine shaft. Normally K1 + K3 + K5 + K7 = 1.0 and K2 + K4 + K6 + K8 = 1.0 (if second generator is present).
    - The division of power between the two shafts is in proportion to the values of MVA bases of the two generators. The initial condition load flow should, therefore, have the two generators loaded to the same fraction of each one's MVA base.
    """

    def __init__(self):
        super().__init__()
        self.k = PU(25)  # Governor gain (reciprocal of droop) (K) (> 0).  Typical Value = 25.
        self.k1 = 0.2  # Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2.
        self.k2 = 0  # Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0.
        self.k3 = 0.3  # Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3.
        self.k4 = 0  # Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0.
        self.k5 = 0.5  # Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5.
        self.k6 = 0  # Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0.
        self.k7 = 0  # Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0.
        self.k8 = 0  # Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0.
        self.mwbase = ActivePower()  # Base for power values (MWbase) (> 0).
        self.pmax = PU(1)  # Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1.
        self.pmin = PU(0)  # Minimum valve opening (Pmin) (>= 0).  Typical Value = 0.
        self.t1 = Seconds(0)  # Governor lag time constant (T1).  Typical Value = 0.
        self.t2 = Seconds(0)  # Governor lead time constant (T2).  Typical Value = 0.
        self.t3 = Seconds(0.1)  # Valve positioner time constant (T3) (> 0).  Typical Value = 0.1.
        self.t4 = Seconds(0.3)  # Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3.
        self.t5 = Seconds(5)  # Time constant of second boiler pass (T5).  Typical Value = 5.
        self.t6 = Seconds(0.5)  # Time constant of third boiler pass (T6).  Typical Value = 0.5.
        self.t7 = Seconds(0)  # Time constant of fourth boiler pass (T7).  Typical Value = 0.
        self.uc = -10  # Maximum valve closing velocity (Uc) (< 0).  Unit = PU/sec.  Typical Value = -
