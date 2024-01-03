# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamFV2(TurbineGovernorDynamics):
    """Steam turbine governor with reheat time constants and modeling of the effects
    of fast valve closing to reduce mechanical power.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        """Constructor for GovSteamFV2"""
        super().__init__()
        self.dt: float = 1.0  # (Dt)
        self.k: float = 1.0  # Fraction of the turbine power developed by turbine sections not involved in fast valving (K)
        self.mw_base: float = 1.0  # Alternate Base used instead of Machine base in equipment model if necessary (MWbase) (>0), Unit = MW
        self.r: float = 1.0  # (R)
        self.t1: Seconds = Seconds() # Governor time constant (T1)
        self.t3: Seconds = Seconds() # Reheater time constant (T3)
        self.ta: Seconds = Seconds() # Time after initial time for valve to close (Ta)
        self.tb: Seconds = Seconds() # Time after initial time for valve to begin opening (Tb)
        self.tc: Seconds = Seconds() # Time after initial time for valve to become fully open (Tc)
        self.ti: Seconds = Seconds() # Initial time to begin fast valving (Ti)
        self.tt: Seconds = Seconds() # Time constant with which power falls off after intercept valve closure (Tt)
        self.vmax: float = 1.0  # (Vmax)
        self.vmin: float = 1.0  # (Vmin)
