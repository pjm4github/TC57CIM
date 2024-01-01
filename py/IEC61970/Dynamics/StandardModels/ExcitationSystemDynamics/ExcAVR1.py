# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAvr1(ExcitationSystemDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.e1: Optional[PU] = PU()  # Field voltage value 1 (E1). Typical Value = 4.18.
        self.e2: Optional[PU] = PU()  # Field voltage value 2 (E2). Typical Value = 3.14.
        self.ka: Optional[float] = 1.0  # AVR gain (K_A). Typical Value = 500.
        self.kf: Optional[float] = 1.0  # Rate feedback gain (K_F). Typical Value = 0.12.
        self.se1: Optional[float] = 1.0  # Saturation factor at E1 (S(E1)). Typical Value = 0.1.
        self.se2: Optional[float] = 1.0  # Saturation factor at E2 (S(E2)). Typical Value = 0.03.
        self.ta: Optional[Seconds] = Seconds()  # AVR time constant (T_A). Typical Value = 0.2.
        self.tb: Optional[Seconds] = Seconds()  # AVR time constant (T_B). Typical Value = 0.
        self.te: Optional[Seconds] = Seconds()  # Exciter time constant (T_E). Typical Value = 1.
        self.tf: Optional[Seconds] = Seconds()  # Rate feedback time constant (T_F). Typical Value = 1.
        self.vrmn: Optional[PU] = PU()  # Minimum AVR output (V_RMN). Typical Value = -6.
        self.vrmx: Optional[PU] = PU()  # Maximum AVR output (V_RMX). Typical Value = 7.
