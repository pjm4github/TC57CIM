# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional


class ExcAvr2:
    """
    Italian excitation system corresponding to IEEE (1968) Type 2 Model. It
    represents alternator and rotating diodes and electromechanic voltage
    regulators.
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.e1: Optional[float] = 1.0  # Field voltage value 1 (E1). Typical Value = 4.18.
        self.e2: Optional[float] = 1.0  # Field voltage value 2 (E2). Typical Value = 3.14.
        self.ka: Optional[float] = 1.0  # AVR gain (K_A). Typical Value = 500.
        self.kf: Optional[float] = 1.0  # Rate feedback gain (K_F). Typical Value = 0.12.
        self.se1: Optional[float] = 1.0  # Saturation factor at E1 (S(E1)). Typical Value = 0.1.
        self.se2: Optional[float] = 1.0  # Saturation factor at E2 (S(E2)). Typical Value = 0.03.
        self.ta: Optional[float] = 1.0  # AVR time constant (T_A). Typical Value = 0.02.
        self.tb: Optional[float] = 1.0  # AVR time constant (T_B). Typical Value = 0.
        self.te: Optional[float] = 1.0  # Exciter time constant (T_E). Typical Value = 1.
        self.tf1: Optional[float] = 1.0  # Rate feedback time constant (T_F1). Typical Value = 1.
        self.tf2: Optional[float] = 1.0  # Rate feedback time constant (T_F2). Typical Value = 1.
        self.vrmn: Optional[float] = 1.0  # Minimum AVR output (V_RMN). Typical Value = -6.
        self.vrmx: Optional[float] = 1.0  # Maximum AVR output (V_RMX). Typical Value = 7.
