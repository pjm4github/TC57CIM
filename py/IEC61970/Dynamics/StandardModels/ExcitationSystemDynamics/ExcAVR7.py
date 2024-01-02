# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from datetime import datetime
from typing import Any

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAvr7(ExcitationSystemDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.a1: Any = 0.5  # Lead coefficient (A1).  Typical Value = 0.5.
        self.a2: Any = 0.5  # Lag coefficient (A2).  Typical Value = 0.5.
        self.a3: Any = 0.5  # Lead coefficient (A3).  Typical Value = 0.5.
        self.a4: Any = 0.5  # Lag coefficient (A4).  Typical Value = 0.5.
        self.a5: Any = 0.5  # Lead coefficient (A5).  Typical Value = 0.5.
        self.a6: Any = 0.5  # Lag coefficient (A6).  Typical Value = 0.5.
        self.k1: Any = 1.0  # Gain (K1).  Typical Value = 1.
        self.k3: Any = 3.0  # Gain (K3).  Typical Value = 3.
        self.k5: Any = 1.0  # Gain (K5).  Typical Value = 1.
        self.t1: Seconds = Seconds(0.05) # Lead time constant (T1).  Typical Value = 0.05.
        self.t2: Seconds = Seconds(.1) # Lag time constant (T2).  Typical Value = 0.1.
        self.t3: Seconds = Seconds(.1) # Lead time constant (T3).  Typical Value = 0.1.
        self.t4: Seconds = Seconds(.1) # Lag time constant (T4).  Typical Value = 0.1.
        self.t5: Seconds = Seconds(.1) # Lead time constant (T5).  Typical Value = 0.1.
        self.t6: Seconds = Seconds(.1) # Lag time constant (T6).  Typical Value = 0.1.
        self.vmax1: Any = 5.0  # Lead-lag max. limit (Vmax1).  Typical Value = 5.
        self.vmax3: Any = 5.0  # Lead-lag max. limit (Vmax3).  Typical Value = 5.
        self.vmax5: Any = 5.0  # Lead-lag max. limit (Vmax5).  Typical Value = 5.
        self.vmin1: Any = -5.0  # Lead-lag min. limit (Vmin1).  Typical Value = -5.
        self.vmin3: Any = -5.0  # Lead-lag min. limit (Vmin3).  Typical Value = -5.
        self.vmin5: Any = -2.  # Lead-lag min. limit (Vmin5).  Typical Value = -2.

