# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAc1A(ExcitationSystemDynamics):
    """
    Modified IEEE AC1A alternator-supplied rectifier excitation system with different rate feedback source.
    """

    def __init__(self) -> None:
        super().__init__()
        self.hvlv_gates: Optional[bool] = False  # Indicates if both HV gate and LV gate are active (HVLVgates). True = gates are used, False = gates are not used. Typical Value = True.
        self.ka: Optional[float] = 1.0  # Voltage regulator gain (Ka). Typical Value = 400.
        self.kc: Optional[float] = 1.0  # Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.2.
        self.kd: Optional[float] = 1.0  # Demagnetizing factor, a function of exciter alternator reactances (Kd). Typical Value = 0.38.
        self.ke: Optional[float] = 1.0  # Exciter constant related to self-excited field (Ke). Typical Value = 1.
        self.kf: Optional[float] = 1.0  # Excitation control system stabilizer gains (Kf). Typical Value = 0.03.
        self.kf1: Optional[float] = 1.0  # Coefficient to allow different usage of the model (Kf1). Typical Value = 0.
        self.kf2: Optional[float] = 1.0  # Coefficient to allow different usage of the model (Kf2). Typical Value = 1.
        self.ks: Optional[float] = 1.0  # Coefficient to allow different usage of the model-speed coefficient (Ks). Typical Value = 0.
        self.se_ve1: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]). Typical Value = 0.1.
        self.se_ve2: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]). Typical Value = 0.03.
        self.ta: Optional[float] = 1.0  # Voltage regulator time constant (Ta). Typical Value = 0.02.
        self.tb: Optional[float] = 1.0  # Voltage regulator time constant (Tb). Typical Value = 0.
        self.tc: Optional[float] = 1.0  # Voltage regulator time constant (Tc). Typical Value = 0.
        self.te: Optional[float] = 1.0  # Exciter time constant, integration rate associated with exciter control (Te). Typical Value = 0.8.
        self.tf: Optional[float] = 1.0  # Excitation control system stabilizer time constant (Tf). Typical Value = 1.
        self.vamax: Optional[float] = 1.0  # Maximum voltage regulator output (Vamax). Typical Value = 14.5.
        self.vamin: Optional[float] = 1.0  # Minimum voltage regulator output (Vamin). Typical Value = -14.5.
        self.ve1: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1). Typical Value = 4.18.
        self.ve2: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2). Typical Value = 3.14.
        self.vrmax: Optional[float] = 1.0  # Maximum voltage regulator outputs (Vrmax). Typical Value = 6.03.
        self.vrmin: Optional[float] = 1.0  # Minimum voltage regulator outputs (Rrmin). Typical Value = -5.43.
