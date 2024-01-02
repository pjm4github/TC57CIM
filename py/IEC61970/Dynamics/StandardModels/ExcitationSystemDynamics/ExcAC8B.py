# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds


class ExcAc8B:
    """
    Modified IEEE AC8B alternator-supplied rectifier excitation system with speed
    input and input limiter.
    """

    def __init__(self) -> None:
        """
        Constructor for ExcAC8B class.
        """
        self.in_lim: bool = False  # Input limiter indicator
        self.ka: float = 1.0  # Voltage regulator gain (Ka)
        self.kc: float = 1.0  # Rectifier loading factor proportional to commutating reactance (Kc)
        self.kd: float = 1.0  # Demagnetizing factor, a function of exciter alternator reactances (Kd)
        self.kdr: float = 1.0  # Voltage regulator derivative gain (Kdr)
        self.ke: float = 1.0  # Exciter constant related to self-excited field (Ke)
        self.kir: float = 1.0  # Voltage regulator integral gain (Kir)
        self.kpr: float = 1.0  # Voltage regulator proportional gain (Kpr)
        self.ks: float = 1.0  # Coefficient to allow different usage of the model-speed coefficient (Ks)
        self.pid_lim: bool = False  # PID limiter indicator
        self.se_ve1: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve1
        self.se_ve2: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve2
        self.ta: Seconds = Seconds() # Voltage regulator time constant (Ta)
        self.tdr: Seconds = Seconds() # Lag time constant (Tdr)
        self.te: Seconds = Seconds() # Exciter time constant, integration rate associated with exciter control (Te)
        self.telim: bool = False  # Selector for the limiter on the block [1/sTe]
        self.ve1: float = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1)
        self.ve2: float = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2)
        self.vemin: float = 1.0  # Minimum exciter voltage output (Vemin)
        self.vfemax: float = 1.0  # Exciter field current limit reference (Vfemax)
        self.vimax: float = 1.0  # Input signal maximum (Vimax)
        self.vimin: float = 1.0  # Input signal minimum (Vimin)
        self.vpidmax: float = 1.0  # PID maximum controller output (Vpidmax)
        self.vpidmin: float = 1.0  # PID minimum controller output (Vpidmin)
        self.vrmax: float = 1.0  # Maximum voltage regulator output (Vrmax)
        self.vrmin: float = 1.0  # Minimum voltage regulator output (Vrmin)
        self.vt_mult: bool = False  # Multiply by generator's terminal voltage indicator
