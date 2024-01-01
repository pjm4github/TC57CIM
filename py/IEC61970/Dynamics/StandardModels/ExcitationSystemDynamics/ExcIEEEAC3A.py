# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC3A model. The model represents
    the field-controlled alternator-rectifier excitation systems designated Type
    AC3A. These excitation systems include an alternator main exciter with non-
    controlled rectifiers. The exciter employs self-excitation, and the voltage
    regulator power is derived from the exciter output voltage. Therefore, this
    system has an additional nonlinearity, simulated by the use of a multiplier
    whose inputs are the voltage regulator command signal, Va, and the
    exciter output voltage, Efd, times K_R. This model is applicable to
    excitation systems employing static voltage regulators.

    Reference: IEEE Standard 421.5-2005 Section 6.3.
    """

    def __init__(self) -> None:
        """
        Value of EFDN at which feedback gain changes (E_FDN). Typical
        Value = 2.36.
        """
        super().__init__()
        self.efdn: Optional[PU] = PU()
        """
        Voltage regulator gain (K_A). Typical Value = 45.62.
        """
        self.ka: Optional[PU] = PU()
        """
        Rectifier loading factor proportional to commutating reactance (K_C).
        Typical Value = 0.104.
        """
        self.kc: Optional[PU] = PU()
        """
        Demagnetizing factor, a function of exciter alternator reactances
        (K_D). Typical Value = 0.499.
        """
        self.kd: Optional[PU] = PU()
        """
        Exciter constant related to self-excited field (K_E). Typical Value
        = 1.
        """
        self.ke: Optional[PU] = PU()
        """
        Excitation control system stabilizer gains (K_F). Typical Value
        = 0.143.
        """
        self.kf: Optional[PU] = PU()
        """
        Excitation control system stabilizer gain (K_N). Typical Value
        = 0.05.
        """
        self.kn: Optional[PU] = PU()
        """
        Constant associated with regulator and alternator field power supply
        (K_R). Typical Value = 3.77.
        """
        self.kr: Optional[PU] = PU()
        """
        Exciter saturation function value at the corresponding exciter
        voltage, V_E1, back of commutating reactance (S_E[V_E1]). Typical
        Value = 1.143.
        """
        self.seve1: Optional[float] = 1.0
        """
        Exciter saturation function value at the corresponding exciter
        voltage, V_E2, back of commutating reactance (S_E[V_E2]). Typical
        Value = 0.1.
        """
        self.seve2: Optional[float] = 1.0
        """
        Voltage regulator time constant (T_A). Typical Value = 0.013.
        """
        self.ta: Optional[Seconds] = Seconds()
        """
        Voltage regulator time constant (T_B). Typical Value = 0.
        """
        self.tb: Optional[Seconds] = Seconds()
        """
        Voltage regulator time constant (T_C). Typical Value = 0.
        """
        self.tc: Optional[Seconds] = Seconds()
        """
        Exciter time constant, integration rate associated with exciter control
        (T_E). Typical Value = 1.17.
        """
        self.te: Optional[Seconds] = Seconds()
        """
        Excitation control system stabilizer time constant (T_F). Typical
        Value = 1.
        """
        self.tf: Optional[Seconds] = Seconds()
        """
        Maximum voltage regulator output (V_AMAX). Typical Value = 1.
        """
        self.vamax: Optional[PU] = PU()
        """
        Minimum voltage regulator output (V_AMIN). Typical Value = -0.95.
        """
        self.vamin: Optional[PU] = PU()
        """
        Exciter alternator output voltages back of commutating reactance at which
        saturation is defined (V_E1) equals V_EMAX (V_E1). Typical Value
        = 6.24.
        """
        self.ve1: Optional[PU] = PU()
        """
        Exciter alternator output voltages back of commutating reactance at which
        saturation is defined (V_E2). Typical Value = 4.68.
        """
        self.ve2: Optional[PU] = PU()
        """
        Minimum exciter voltage output (V_EMIN). Typical Value = 0.1.
        """
        self.vemin: Optional[PU] = PU()
        """
        Exciter field current limit reference (V_FEMAX). Typical Value = 16.
        """
        self.vfemax: Optional[PU] = PU()
