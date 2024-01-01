# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:00:52 2023
from typing import Any

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import \
    OverexcitationLimiterDynamics


class OverexcLimX1(OverexcitationLimiterDynamics):
    """
    Field voltage over excitation limiter.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # Low voltage point on the inverse time characteristic (EFD<sub>1</sub>).
        # Typical Value = 1.1.
        super().__init__()
        self.efd1: PU = PU(1.1)

        # Mid voltage point on the inverse time characteristic (EFD<sub>2</sub>).
        # Typical Value = 1.2.
        self.efd2: PU = PU(1.2)

        # High voltage point on the inverse time characteristic (EFD<sub>3</sub>).
        # Typical Value = 1.5.
        self.efd3: PU = PU(1.5)

        # Desired field voltage (EFD<sub>DES</sub>).  Typical Value = 0.9.
        self.efddes: PU = PU(0.9)

        # Rated field voltage (EFD<sub>RATED</sub>).  Typical Value = 1.05.
        self.efdrated: PU = PU(1.05)

        # Gain (K<sub>MX</sub>).  Typical Value = 0.01.
        self.kmx: PU = PU(0.01)

        # Time to trip the exciter at the low voltage point on the inverse time
        # characteristic (TIME<sub>1</sub>).  Typical Value = 120.
        self.t1: Seconds = Seconds(120)

        # Time to trip the exciter at the mid voltage point on the inverse time
        # characteristic (TIME<sub>2</sub>).  Typical Value = 40.
        self.t2: Seconds = Seconds(40)

        # Time to trip the exciter at the high voltage point on the inverse time
        # characteristic (TIME<sub>3</sub>).  Typical Value = 15.
        self.t3: Seconds = Seconds(15)

        # Low voltage limit (V<sub>LOW</sub>) (>0).
        self.vlow: PU = PU(.1)
