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
        self.efdmax: PU = PU()  # Exciter output maximum limit (Efdmax)
        self.efdmin: PU = PU()  # Exciter output minimum limit (Efdmin)
        self.ka: PU = PU()  # Regulator gain (Ka)
        self.ke: PU = PU()  # Exciter constant related to self-excited field (Ke)
        self.kp: PU = PU()  # Regulator proportional gain (Kp)
        self.ta: Seconds = Seconds()  # Regulator time constant (Ta)
        self.tc: Seconds = Seconds()  # Regulator integral time constant (Tc)
        self.te: Seconds = Seconds()  # Exciter time constant, integration rate associated with exciter control (Te)
        self.vrmax: PU = PU()  # Voltage regulator maximum limit (Vrmax)
        self.vrmin: PU = PU()  # Voltage regulator minimum limit (Vrmin)
