# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroIeee2(TurbineGovernorDynamics):
    """
    IEEE hydro turbine governor model represents plants with straightforward
    penstock configurations and hydraulic-dashpot governors.

    Reference: IEEE Transactions on Power Apparatus and
    Systems November/December 1973, Volume PAS-92, Number 6
    <i><u>Dynamic Models for Steam and Hydro Turbines in
    Power System Studies</u></i>, Page 1904.

    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.aturb = PU(-1)  # Turbine numerator multiplier (Aturb).  Typical Value = -1.
        self.bturb = PU(.5)  # Turbine denominator multiplier (Bturb).  Typical Value = 0.5.
        self.gv1 = PU(0)  # Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
        self.gv2 = PU(0)  # Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
        self.gv3 = PU(0)  # Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
        self.gv4 = PU(0)  # Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
        self.gv5 = PU(0)  # Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
        self.gv6 = PU(0)  # Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
        self.kturb = PU(1)  # Turbine gain (Kturb).  Typical Value = 1.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (> 0).  Unit = MW.
        self.pgv1 = PU(0)  # Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
        self.pgv2 = PU(0)  # Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
        self.pgv3 = PU(0)  # Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
        self.pgv4 = PU(0)  # Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
        self.pgv5 = PU(0)  # Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
        self.pgv6 = PU(0)  # Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
        self.pmax = PU(1)  # Maximum gate opening (Pmax).  Typical Value = 1.
        self.pmin = PU(0)  # Minimum gate opening (Pmin).  Typical Value = 0.
        self.rperm = PU(.05)  # Permanent droop (Rperm).  Typical Value = 0.05.
        self.rtemp = PU(.5)  # Temporary droop (Rtemp).  Typical Value = 0.5.
        self.tg = Seconds(.5)  # Gate servo time constant (Tg).  Typical Value = 0.5.
        self.tp = Seconds(.03)  # Pilot servo valve time constant (Tp).  Typical Value = 0.03.
        self.tr = Seconds(12)  # Dashpot time constant (Tr).  Typical Value = 12.
        self.tw = Seconds(2)  # Water inertia time constant (Tw).  Typical Value = 2.
        self.uc: float = -0.1  # Maximum gate closing velocity (Uc) (<0).  Typical Value = -0.1.
        self.uo: float = 0.1  # Maximum gate opening velocity (Uo). Unit = PU/sec.  Typical Value = 0.1.
