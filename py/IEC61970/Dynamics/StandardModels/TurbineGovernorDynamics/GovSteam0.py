# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam0(TurbineGovernorDynamics):
    """
    A simplified steam turbine governor model.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self):
        super().__init__()
        self.dt = PU(0)  # Turbine damping coefficient (Dt).  Unit = delta P / delta speed. Typical Value = 0.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase)  (>0).  Unit = MW.
        self.r = PU(.05)  # Permanent droop (R).  Typical Value = 0.05.
        self.t1 = Seconds(.5)  # Steam bowl time constant (T1).  Typical Value = 0.5.
        self.t2 = Seconds(3)  # Numerator time constant of T2/T3 block (T2).  Typical Value = 3.
        self.t3 = Seconds(10)  # Reheater time constant (T3).  Typical Value = 10.
        self.vmax = PU(1)  # Maximum valve position, PU of mwcap (Vmax).  Typical Value = 1.
        self.vmin = PU(0)  # Minimum valve position, PU of mwcap (Vmin).  Typical Value = 0.
