# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAns(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents static field voltage or excitation
    current feedback excitation system.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ExcANS
        """
        super().__init__()
        self.blint: Optional[int] = 0  # Governor Control Flag (BLINT).
        # 0 = lead-lag regulator
        # 1 = proportional integral regulator.
        # Typical Value = 0.

        self.ifmn: float = 1.0  # Minimum exciter current (IFMN).  Typical Value = -5.2.

        self.ifmx: float = 1.0  # Maximum exciter current (IFMX).  Typical Value = 6.5.

        self.k2: float = 1.0  # Exciter gain (K2).  Typical Value = 20.

        self.k3: float = 1.0  # AVR gain (K3).  Typical Value = 1000.

        self.kce: float = 1.0  # Ceiling factor (KCE).  Typical Value = 1.

        self.krvecc: Optional[int] = 0  # Feedback enabling (KRVECC).
        # 0 = Open loop control
        # 1 = Closed loop control.
        # Typical Value = 1.

        self.kvfif: Optional[int] = 0  # Rate feedback signal flag (KVFIF).
        # 0 = output voltage of the exciter
        # 1 = exciter field current.
        # Typical Value = 0.

        self.t1: Seconds = Seconds(20)  # Time constant (T1).  Typical Value = 20.

        self.t2: Seconds = Seconds(0.05)  # Time constant (T2).  Typical Value = 0.05.

        self.t3: Seconds = Seconds(1.6)  # Time constant (T3).  Typical Value = 1.6.

        self.tb: Seconds = Seconds(.04)  # Exciter time constant (TB).  Typical Value = 0.04.

        self.vrmn: float = 1.0  # Minimum AVR output (VRMN).  Typical Value = -5.2.

        self.vrmx: float = 1.0  # Maximum AVR output (VRMX).  Typical Value = 6.5.
