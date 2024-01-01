# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeDc2A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC2A model. This model represents
    field-controlled dc commutator exciters with continuously acting
    voltage regulators having supplies obtained from the generator or auxiliary bus.
    It differs from the Type DC1A model only in the voltage regulator output
    limits, which are now proportional to terminal voltage V_T.
    It is representative of solid-state replacements for various forms of older
    mechanical and rotating amplifier regulating equipment connected to dc
    commutator exciters.
    Reference: IEEE Standard 421.5-2005 Section 5.2.
    """

    def __init__(self) -> None:
        super().__init__()
        self.efd1: Optional[float] = 0.0  # Exciter voltage at which exciter saturation is defined (E_FD1). Typical Value = 3.05
        self.efd2: Optional[float] = 0.0  # Exciter voltage at which exciter saturation is defined (E_FD2). Typical Value = 2.29
        self.exclim: Optional[float] = 0.0  # (exclim). IEEE standard is ambiguous about lowering limit on exciter output. Typical Value = -999 which means that there is no limit applied.
        self.ka: Optional[float] = 0.0  # Voltage regulator gain (K_A). Typical Value = 300
        self.ke: Optional[float] = 0.0  # Exciter constant related to self-excited field (K_E). Typical Value = 1
        self.kf: Optional[float] = 0.0  # Excitation control system stabilizer gain (K_F). Typical Value = 0.1
        self.seefd1: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, E_FD1 (S_E[E_FD1]). Typical Value = 0.279
        self.seefd2: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, E_FD2 (S_E[E_FD2]). Typical Value = 0.117
        self.ta: Optional[float] = 0.0  # Voltage regulator time constant (T_A). Typical Value = 0.01
        self.tb: Optional[float] = 0.0  # Voltage regulator time constant (T_B). Typical Value = 0
        self.tc: Optional[float] = 0.0  # Voltage regulator time constant (T_C). Typical Value = 0
        self.te: Optional[float] = 0.0  # Exciter time constant, integration rate associated with exciter control (T_E). Typical Value = 1.33
        self.tf: Optional[float] = 0.0  # Excitation control system stabilizer time constant (T_F). Typical Value = 0.675
        self.uelin: Optional[bool] = False  # UEL input (uelin). true = input is connected to the HV gate, false = input connects to the error signal. Typical Value = True
        self.vrmax: Optional[float] = 0.0  # Maximum voltage regulator output (V_RMAX). Typical Value = 4.95
        self.vrmin: Optional[float] = 0.0  # Minimum voltage regulator output (V_RMIN). Typical Value = -4.9
