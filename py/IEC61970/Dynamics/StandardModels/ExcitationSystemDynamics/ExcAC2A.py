# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds


class ExcAc2A:
    """
    Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.
    """

    def __init__(self) -> None:
        self.hv_gate: bool = False  # Indicates if HV gate is active (HVgate).
        self.ka: float = 0.0  # Voltage regulator gain (Ka). Typical Value = 400.
        self.kb: float = 0.0  # Second stage regulator gain (Kb) (>0). Exciter field current controller gain. Typical
        # Value = 25.
        self.kb1: float = 0.0  # Second stage regulator gain (Kb1). It is exciter field current controller gain
        self.kc: float = 0.0  # Rectifier loading factor proportional to commutating reactance (Kc). Typical Value =
        # 0.28.
        self.kd: float = 0.0  # Demagnetizing factor, a function of exciter alternator reactances (Kd). Typical Value
        # = 0.35.
        self.ke: float = 0.0  # Exciter constant related to self-excited field (Ke). Typical Value = 1.
        self.kf: float = 0.0  # Excitation control system stabilizer gains (Kf). Typical Value = 0.03.
        self.kh: float = 0.0  # Exciter field current feedback gain (Kh). Typical Value = 1.
        self.kl: float = 0.0  # Exciter field current limiter gain (Kl). Typical Value = 10.
        self.kl1: float = 0.0  # Coefficient to allow different usage of the model (Kl1). Typical Value = 1.
        self.ks: float = 0.0  # Coefficient to allow different usage of the model-speed coefficient (Ks). Typical
        # Value = 0.
        self.lv_gate: bool = False  # Indicates if LV gate is active (LVgate). Typical Value = True.
        self.se_ve1: float = 0.0  # Exciter saturation function value at the corresponding exciter voltage,
        # Ve1 (Se[Ve1]). Typical Value = 0.037.
        self.se_ve2: float = 0.0  # Exciter saturation function value at the corresponding exciter voltage,
        # Ve2 (Se[Ve2]). Typical Value = 0.012.
        self.ta: Seconds = Seconds()  # Voltage regulator time constant (Ta). Typical Value = 0.02.
        self.tb: Seconds = Seconds()  # Voltage regulator time constant (Tb). Typical Value = 0.
        self.tc: Seconds = Seconds()  # Voltage regulator time constant (Tc). Typical Value = 0.
        self.te: Seconds = Seconds()  # Exciter time constant, integration rate associated with exciter control (Te).
        # Typical Value = 0.6.
        self.tf: Seconds = Seconds()  # Excitation control system stabilizer time constant (Tf). Typical Value = 1.
        self.va_max: float = 0.0  # Maximum voltage regulator output (Va_max). Typical Value = 8.
        self.va_min: float = 0.0  # Minimum voltage regulator output (Va_min). Typical Value = -8.
        self.ve1: float = 0.0  # Exciter alternator output voltages back of commutating reactance at which saturation
        # is defined (Ve1). Typical Value = 4.4.
        self.ve2: float = 0.0  # Exciter alternator output voltages back of commutating reactance at which saturation
        # is defined (Ve2). Typical Value = 3.3.
        self.vfe_max: float = 0.0  # Exciter field current limit reference (Vfemax). Typical Value = 4.4.
        self.vlr: float = 0.0  # Maximum exciter field current (Vlr). Typical Value = 4.4.
        self.vr_max: float = 0.0  # Maximum voltage regulator outputs (Vrmax). Typical Value = 105.
        self.vr_min: float = 0.0  # Minimum voltage regulator outputs (Vrmin). Typical Value = -95.
