# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam2(TurbineGovernorDynamics):
    """
    Simplified governor model.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.dbf: PU = PU(0)  # Frequency dead band (DBF).  Typical Value = 0.
        self.k: float = 20.0  # Governor gain (reciprocal of droop) (K).  Typical Value = 20.
        self.mnef: PU = PU(-1)  # Fuel flow maximum negative error value (MN<sub>EF<sub>).  Typical Value = -1.
        self.mxef: PU = PU(1)  # Fuel flow maximum positive error value (MX<sub>EF<sub>).  Typical Value = 1.
        self.pmax: PU = PU(1)  # Maximum fuel flow (P<sub>MAX<sub>).  Typical Value = 1.
        self.pmin: PU = PU(0)  # Minimum fuel flow (P<sub>MIN<sub>).  Typical Value = 0.
        self.t1: Seconds = Seconds(.45)  # Governor lag time constant (T<sub>1<sub>) (>0).  Typical Value = 0.45.
        self.t2: Seconds = Seconds(0)  # Governor lead time constant (T<sub>2<sub>) (may be 0).  Typical Value = 0.
