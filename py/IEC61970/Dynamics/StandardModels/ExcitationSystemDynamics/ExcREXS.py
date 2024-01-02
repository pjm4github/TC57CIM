# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds


class ExcRexs:
    """
    General Purpose Rotating Excitation System Model.  This model can be used to
    represent a wide range of excitation systems whose DC power source is an AC or
    DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system
    models.
    """

    def __init__(self) -> None:
        """Constructor"""
        self.e1: float = 3.0  # Field voltage value 1 (E1). Typical Value = 3.
        self.e2: float = 4.0  # Field voltage value 2 (E2). Typical Value = 4.
        self.fbf: Optional[str] = "fieldCurrent"  # Rate feedback signal flag (Fbf). Typical Value = fieldCurrent.
        self.flimf: float = 0.0  # Limit type flag (Flimf). Typical Value = 0.
        self.kc: float = 0.05  # Rectifier regulation factor (Kc). Typical Value = 0.05.
        self.kd: float = 2.0  # Exciter regulation factor (Kd). Typical Value = 2.
        self.ke: float = 1.0  # Exciter field proportional constant (Ke). Typical Value = 1.
        self.kefd: float = 0.0  # Field voltage feedback gain (Kefd). Typical Value = 0.
        self.kf: float = 0.05  # Rate feedback gain (Kf). Typical Value = 0.05.
        self.kh: float = 0.0  # Field voltage controller feedback gain (Kh). Typical Value = 0.
        self.kii: float = 0.0  # Field Current Regulator Integral Gain (Kii). Typical Value = 0.
        self.kip: float = 1.0  # Field Current Regulator Proportional Gain (Kip). Typical Value = 1.
        self.ks: float = 0.0  # Coefficient to allow different usage of the model-speed coefficient (Ks). Typical Value = 0.
        self.kvi: float = 0.0 # Voltage Regulator Integral Gain (Kvi). Typical Value = 0.
        self.kvp: float = 2800.0  # Voltage Regulator Proportional Gain (Kvp). Typical Value = 2800.
        self.kvphz: float = 0.0  # V/Hz limiter gain (Kvphz). Typical Value = 0.
        self.nvphz: float = 0.0  # Pickup speed of V/Hz limiter (Nvphz). Typical Value = 0.
        self.se1: float = 0.0001  # Saturation factor at E1 (Se1). Typical Value = 0.0001.
        self.se2: float = 0.001  # Saturation factor at E2 (Se2). Typical Value = 0.001.
        self.ta: Seconds = Seconds(0.01) # Voltage Regulator time constant (Ta). Typical Value = 0.01.
        self.tb1: Seconds = Seconds(0) # Lag time constant (Tb1). Typical Value = 0.
        self.tb2: Seconds = Seconds(0) # Lag time constant (Tb2). Typical Value = 0.
        self.tc1: Seconds = Seconds(0) # Lead time constant (Tc1). Typical Value = 0.
        self.tc2: Seconds = Seconds(0) # Lead time constant (Tc2). Typical Value = 0.
        self.te: Seconds = Seconds(1.2) # Exciter field time constant (Te). Typical Value = 1.2.
        self.tf: Seconds = Seconds(1) # Rate feedback time constant (Tf). Typical Value = 1.
        self.tf1: Seconds = Seconds(0) # Feedback lead time constant (Tf1). Typical Value = 0.
        self.tf2: Seconds = Seconds(0) # Feedback lag time constant (Tf2). Typical Value = 0.
        self.tp: Seconds = Seconds(0) # Field current Bridge time constant (Tp). Typical Value = 0.
        self.vcmax: float = 0.0  # Maximum compounding voltage (Vcmax). Typical Value = 0.
        self.vfmax: float = 47.0  # Maximum Exciter Field Current (Vfmax). Typical Value = 47.
        self.vfmin: float = -20.0  # Minimum Exciter Field Current (Vfmin). Typical Value = -20.
        self.vimax: float = 0.1  # Voltage Regulator Input Limit (Vimax). Typical Value = 0.1.
        self.vrmax: float = 47.0  # Maximum controller output (Vrmax). Typical Value = 47.
        self.vrmin: float = -20.0  # Minimum controller output (Vrmin). Typical Value = -20.
        self.xc: float = 0.0 # Exciter compounding reactance (Xc). Typical Value = 0.
