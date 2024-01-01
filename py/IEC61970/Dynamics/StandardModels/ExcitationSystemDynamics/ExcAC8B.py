# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional


class ExcAc8B:
    """
    Modified IEEE AC8B alternator-supplied rectifier excitation system with speed
    input and input limiter.
    """

    def __init__(self) -> None:
        """
        Constructor for ExcAC8B class.
        """
        self.in_lim: Optional[bool] = False  # Input limiter indicator
        self.ka: Optional[float] = 1.0  # Voltage regulator gain (Ka)
        self.kc: Optional[float] = 1.0  # Rectifier loading factor proportional to commutating reactance (Kc)
        self.kd: Optional[float] = 1.0  # Demagnetizing factor, a function of exciter alternator reactances (Kd)
        self.kdr: Optional[float] = 1.0  # Voltage regulator derivative gain (Kdr)
        self.ke: Optional[float] = 1.0  # Exciter constant related to self-excited field (Ke)
        self.kir: Optional[float] = 1.0  # Voltage regulator integral gain (Kir)
        self.kpr: Optional[float] = 1.0  # Voltage regulator proportional gain (Kpr)
        self.ks: Optional[float] = 1.0  # Coefficient to allow different usage of the model-speed coefficient (Ks)
        self.pid_lim: Optional[bool] = False  # PID limiter indicator
        self.se_ve1: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve1
        self.se_ve2: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve2
        self.ta: Optional[float] = 1.0  # Voltage regulator time constant (Ta)
        self.tdr: Optional[float] = 1.0  # Lag time constant (Tdr)
        self.te: Optional[float] = 1.0  # Exciter time constant, integration rate associated with exciter control (Te)
        self.telim: Optional[bool] = False  # Selector for the limiter on the block [1/sTe]
        self.ve1: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1)
        self.ve2: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2)
        self.vemin: Optional[float] = 1.0  # Minimum exciter voltage output (Vemin)
        self.vfemax: Optional[float] = 1.0  # Exciter field current limit reference (Vfemax)
        self.vimax: Optional[float] = 1.0  # Input signal maximum (Vimax)
        self.vimin: Optional[float] = 1.0  # Input signal minimum (Vimin)
        self.vpidmax: Optional[float] = 1.0  # PID maximum controller output (Vpidmax)
        self.vpidmin: Optional[float] = 1.0  # PID minimum controller output (Vpidmin)
        self.vrmax: Optional[float] = 1.0  # Maximum voltage regulator output (Vrmax)
        self.vrmin: Optional[float] = 1.0  # Minimum voltage regulator output (Vrmin)
        self.vt_mult: Optional[bool] = False  # Multiply by generator's terminal voltage indicator
