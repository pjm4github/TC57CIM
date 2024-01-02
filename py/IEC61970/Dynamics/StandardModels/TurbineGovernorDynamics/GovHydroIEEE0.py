# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds


class GovHydroIeee0:
    """
    IEEE Simplified Hydro Governor-Turbine Model.  Used for Mechanical-Hydraulic
    and Electro-Hydraulic turbine governors, withour without steam feedback.
    Typical values given are for Mechanical-Hydraulic.

    Reference: IEEE Transactions on Power Apparatus and Systems
               November/December 1973, Volume PAS-92, Number 6
               Dynamic Models for Steam and Hydro Turbines in Power System Studies
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        """
        Constructor for the GovHydroIEEE0 class
        """
        self.k: PU = PU(1.0)  # Governor gain (Ki)
        self.mw_base: ActivePower = ActivePower(1.0)  # Base for power values (MWbase) (> 0).  Unit = MW.
        self.p_max: PU = PU(1.0)  # Gate maximum (Pmax)
        self.p_min: PU = PU(1.0)  # Gate minimum (Pmin)
        self.t1: Seconds = Seconds(0.25) # Governor lag time constant (T1).  Typical Value = 0.25.
        self.t2: Seconds = Seconds(0) # Governor lead time constant (T2i).  Typical Value = 0.
        self.t3: Seconds = Seconds(0.1) # Gate actuator time constant (T3).  Typical Value = 0.1.
        self.t4: Seconds = Seconds(0) # Water starting time (T4)
