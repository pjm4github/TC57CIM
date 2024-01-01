# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeDc1A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC1A model. This model represents
    field-controlled dc commutator exciters with continuously acting voltage
    regulators (especially the direct-acting rheostatic, rotating amplifier, and
    magnetic amplifier types). Because this model has been widely implemented by
    the industry, it is sometimes used to represent other types of systems when
    detailed data for them are not available or when a simplified model is required.

    Reference: IEEE Standard 421.5-2005 Section 5.1.
    """

    def __init__(self) -> None:
        """
        Constructor for ExcIEEEDC1A
        """
        super().__init__()
        self.efd1: Optional[float] = 0.0  # Exciter voltage at which exciter saturation is defined (E_FD1). Typical Value = 3.1.
        self.efd2: Optional[float] = 0.0  # Exciter voltage at which exciter saturation is defined (E_FD2). Typical Value = 2.3.
        self.exclim: Optional[bool] = False  # (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
        # true = a lower limit of zero is applied to integrator output.
        # false = a lower limit of zero is not applied to integrator output. Typical Value = true.
        self.ka: Optional[float] = 0.0  # Voltage regulator gain (K_A).  Typical Value = 46.
        self.ke: Optional[float] = 0.0  # Exciter constant related to self-excited field (K_E).  Typical Value = 0.
        self.kf: Optional[float] = 0.0  # Excitation control system stabilizer gain (K_F).  Typical Value = 0.1.
        self.seefd1: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, E_FD1 (S_E[E_FD1]).
        # Typical Value = 0.33.
        self.seefd2: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, E_FD2 (S_E[E_FD2]).
        # Typical Value = 0.1.
        self.ta: Optional[float] = 0.0  # Voltage regulator time constant (T_A).  Typical Value = 0.06.
        self.tb: Optional[float] = 0.0  # Voltage regulator time constant (T_B).  Typical Value = 0.
        self.tc: Optional[float] = 0.0  # Voltage regulator time constant (T_C).  Typical Value = 0.
        self.te: Optional[float] = 0.0  # Exciter time constant, integration rate associated with exciter control (T_E).
        # Typical Value = 0.46.
        self.tf: Optional[float] = 0.0  # Excitation control system stabilizer time constant (T_F).  Typical Value = 1.
        self.uelin: Optional[bool] = False  # UEL input (uelin).
        # true = input is connected to the HV gate
        # false = input connects to the error signal. Typical Value = true.
        self.vrmax: Optional[float] = 0.0  # Maximum voltage regulator output (V_RMAX).  Typical Value = 1.
        self.vrmin: Optional[float] = 0.0  # Minimum voltage regulator output (V_RMIN).  Typical Value = -0.9.
