# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssSk(PowerSystemStabilizerDynamics):
    """
    PSS Slovakian type - three inputs.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.k1: Optional[PU] = PU(-.3)  # Gain P (K1).  Typical Value = -0.3.
        self.k2: Optional[PU] = PU(-.15)   # Gain fe (K2).  Typical Value = -0.15.
        self.k3: Optional[PU] = PU(10)  # Gain If (K3).  Typical Value = 10.
        self.t1: Optional[Seconds] = Seconds(.3)  # Denominator time constant (T1).  Typical Value = 0.3.
        self.t2: Optional[Seconds] = Seconds(.35)   # Filter time constant (T2).  Typical Value = 0.35.
        self.t3: Optional[Seconds] = Seconds(.22)  # Denominator time constant (T3).  Typical Value = 0.22.
        self.t4: Optional[Seconds] = Seconds(.02)  # Filter time constant (T4).  Typical Value = 0.02.
        self.t5: Optional[Seconds] = Seconds(.02)   # Denominator time constant (T5).  Typical Value = 0.02.
        self.t6: Optional[Seconds] = Seconds(.02)  # Filter time constant (T6).  Typical Value = 0.02.
        self.vsmax: Optional[PU] = PU(.4)  # Stabilizer output max limit (Vsmax).  Typical Value = 0.4.
        self.vsmin: Optional[PU] = PU(-.4)   # Stabilizer output min limit (Vsmin).  Typical Value = -0.4.
