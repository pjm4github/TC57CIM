# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcCz(ExcitationSystemDynamics):
    """
    Czech Proportion/Integral Exciter.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.efdmax: Optional[PU] = PU()  # Exciter output maximum limit (Efdmax)
        self.efdmin: Optional[PU] = PU()  # Exciter output minimum limit (Efdmin)
        self.ka: Optional[PU] = PU()  # Regulator gain (Ka)
        self.ke: Optional[PU] = PU()  # Exciter constant related to self-excited field (Ke)
        self.kp: Optional[PU] = PU()  # Regulator proportional gain (Kp)
        self.ta: Optional[Seconds] = Seconds()  # Regulator time constant (Ta)
        self.tc: Optional[Seconds] = Seconds()  # Regulator integral time constant (Tc)
        self.te: Optional[Seconds] = Seconds()  # Exciter time constant, integration rate associated with exciter control (Te)
        self.vrmax: Optional[PU] = PU()  # Voltage regulator maximum limit (Vrmax)
        self.vrmin: Optional[PU] = PU()  # Voltage regulator minimum limit (Vrmin)
