# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeSt2a(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST2A model. Some static systems
    utilize both current and voltage sources (generator terminal quantities) to
    comprise the power source. The regulator controls the exciter output through
    controlled saturation of the power transformer components. These compound-
    source rectifier excitation systems are designated Type ST2A and are
    represented by ExcIEEEST2A.
    
    Reference: IEEE Standard 421.5-2005 Section 7.2.
    """

    def __init__(self) -> None:
        """Constructor for ExcIEEEST2A"""
        super().__init__()
        self.efd_max: Optional[float] = 0.0  # Maximum field voltage (E_FDMax). Typical Value = 99.
        self.ka: Optional[float] = 0.0  # Voltage regulator gain (K_EA). Typical Value = 120.
        self.kc: Optional[float] = 0.0  # Rectifier loading factor proportional to commutating reactance (K_EC). Typical Value = 1.82.
        self.ke: Optional[float] = 0.0  # Exciter constant related to self-excited field (K_EE). Typical Value = 1.
        self.kf: Optional[float] = 0.0  # Excitation control system stabilizer gains (K_EF). Typical Value = 0.05.
        self.ki: Optional[float] = 0.0  # Potential circuit gain coefficient (K_EI). Typical Value = 8.
        self.kp: Optional[float] = 0.0  # Potential circuit gain coefficient (K_EP). Typical Value = 4.88.
        self.ta: Optional[float] = 0.0  # Voltage regulator time constant (T_EA). Typical Value = 0.15.
        self.te: Optional[float] = 0.0  # Exciter time constant, integration rate associated with exciter control (T_EE). Typical Value = 0.5.
        self.tf: Optional[float] = 0.0  # Excitation control system stabilizer time constant (T_EF). Typical Value = 1.
        self.uelin: Optional[bool] = False  # UEL input (UELin). true = HV gate, false = add to error signal. Typical Value = true.
        self.vrmax: Optional[float] = 0.0  # Maximum voltage regulator outputs (V_ERMAX). Typical Value = 1.
        self.vrmin: Optional[float] = 0.0  # Minimum voltage regulator outputs (V_ERMIN). Typical Value = 0.
