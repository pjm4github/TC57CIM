# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC3A model. The model represents
    the field-controlled alternator-rectifier excitation systems designated Type
    AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers.
    The exciter employs self-excitation, and the voltage
    regulator power is derived from the exciter output voltage. Therefore, this
    system has an additional nonlinearity, simulated by the use of a multiplier
    whose inputs are the voltage regulator command signal, Va, and the
    exciter output voltage, Efd, times K_R. This model is applicable to
    excitation systems employing static voltage regulators.

    Reference: IEEE Standard 421.5-2005 Section 6.3.
    """

    def __init__(self) -> None:
        super().__init__()
        self.efdn: PU = PU(2.36)  # Value of EFDN at which feedback gain changes (E_FDN). Typical Value = 2.36.
        self.ka: PU = PU(45.62)  # Voltage regulator gain (K_A). Typical Value = 45.62.
        self.kc: PU = PU(
            0.104)  # Rectifier loading factor proportional to commutating reactance (K_C). Typical Value = 0.104.
        self.kd: PU = PU(
            0.499)  # Demagnetizing factor, a function of exciter alternator reactances.(K_D). Typical Value = 0.499.
        self.ke: PU = PU(1)  # Exciter constant related to self-excited field (K_E). Typical Value = 1.
        self.kf: PU = PU(.143)  # Excitation control system stabilizer gains (K_F). Typical Value = 0.143.
        self.kn: PU = PU(0.05)  # Excitation control system stabilizer gain (K_N). Typical Value = 0.05.
        self.kr: PU = PU(
            3.77)  # Constant associated with regulator and alternator field power supply (K_R). Typical Value = 3.77.
        self.seve1: float = 1.143  # Exciter saturation function value at the corresponding exciter voltage, V_E1,
        # back of commutating reactance (S_E[V_E1]). Typical Value = 1.143.
        self.seve2: float = 0.1  # Exciter saturation function value at the corresponding exciter voltage, V_E2,
        # back of commutating reactance (S_E[V_E2]). Typical Value = 0.1.
        self.ta: Seconds = Seconds(0.013)  # Voltage regulator time constant (T_A). Typical Value = 0.013.
        self.tb: Seconds = Seconds(0)  # Voltage regulator time constant (T_B). Typical Value = 0.
        self.tc: Seconds = Seconds(0)  # Voltage regulator time constant (T_C). Typical Value = 0.
        self.te: Seconds = Seconds(
            1.17)  # Exciter time constant, integration rate associated with exciter control.         (T_E). Typical
        # Value = 1.17.
        self.tf: Seconds = Seconds(1)  # Excitation control system stabilizer time constant (T_F). Typical Value = 1.
        self.vamax: PU = PU(1)  # Maximum voltage regulator output (V_AMAX). Typical Value = 1.
        self.vamin: PU = PU(-.95)  # Minimum voltage regulator output (V_AMIN). Typical Value = -0.95.
        self.ve1: PU = PU(
            6.24)  # Exciter alternator output voltages back of commutating reactance at which saturation is defined
        # (V_E1) equals V_EMAX (V_E1). Typical Value = 6.24.
        self.ve2: PU = PU(
            4.68)  # Exciter alternator output voltages back of commutating reactance at which saturation is defined
        # (V_E2). Typical Value = 4.68.
        self.vemin: PU = PU(.1)  # Minimum exciter voltage output (V_EMIN). Typical Value = 0.1.
        self.vfemax: PU = PU(16)  # Exciter field current limit reference (V_FEMAX). Typical Value = 16.
