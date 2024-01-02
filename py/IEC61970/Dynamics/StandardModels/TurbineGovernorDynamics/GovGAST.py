# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST(TurbineGovernorDynamics):
    """
    Single shaft gas turbine.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """
        Constructor for GovGAST
        """
        super().__init__()
        # Ambient temperature load limit (Load Limit).  Typical Value = 1.
        self.at: PU = PU(1)

        # Turbine damping factor (Dturb).  Typical Value = 0.18.
        self.dturb: PU = PU(0.18)

        # Temperature limiter gain (Kt).  Typical Value = 3.
        self.kt: PU = PU(3)

        # Base for power values (MWbase) (> 0).
        self.mw_base: ActivePower = ActivePower()

        # Permanent droop (R).  Typical Value = 0.04.
        self.r: PU = PU(0.04)

        # Governor mechanism time constant (T1).  T1 represents the natural valve
        # positioning time constant of the governor for small disturbances, as seen when
        # rate limiting is not in effect.  Typical Value = 0.5.
        self.t1: Seconds = Seconds(0.5)

        # Turbine power time constant (T2).  T2 represents delay due to internal energy
        # storage of the gas turbine engine. T2 can be used to give a rough approximation
        # to the delay associated with acceleration of the compressor spool of a multi-
        # shaft engine, or with the compressibility of gas in the plenum of the free
        # power turbine of an aero-derivative unit, for example.  Typical Value = 0.5.
        self.t2: Seconds = Seconds(0.5)

        # Turbine exhaust temperature time constant (T3).  Typical Value = 3.
        self.t3: Seconds = Seconds(3)

        # Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1.
        self.vmax: PU = PU(1.0)

        # Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0.
        self.vmin: PU = PU(0.0)
