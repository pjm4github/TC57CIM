# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Any

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssPTIST1(PowerSystemStabilizerDynamics):
    """
    PTI Microprocessor-Based Stabilizer type 1.
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.dtc: Seconds = Seconds(0.025)  # Time step related to activation of controls (Dtc).  Typical Value = 0.025.
        self.dtf: Seconds = Seconds(0.025)  # Time step frequency calculation (Dtf).  Typical Value = 0.025.
        self.dtp: Seconds = Seconds(0.0125)  # Time step active power calculation (Dtp).  Typical Value = 0.0125.
        self.k: PU = PU(9)  # Gain (K).  Typical Value = 9.
        self.m: PU = PU(5)  # (M).  M=2*H.  Typical Value = 5.
        self.t1: Seconds = Seconds(0.3)  # Time constant (T1).  Typical Value = 0.3.
        self.t2: Seconds = Seconds(1)  # Time constant (T2).  Typical Value = 1.
        self.t3: Seconds = Seconds(.2)  # Time constant (T3).  Typical Value = 0.2.
        self.t4: Seconds = Seconds(.05)  # Time constant (T4).  Typical Value = 0.05.
        self.tf: Seconds = Seconds(.2)  # Time constant (Tf).  Typical Value = 0.2.
        self.tp: Seconds = Seconds(.2)  # Time constant (Tp).  Typical Value = 0.2
