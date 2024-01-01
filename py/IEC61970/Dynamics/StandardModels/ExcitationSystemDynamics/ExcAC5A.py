# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from dataclasses import dataclass
from typing import Optional


@dataclass
class ExcAc5A:
    """
    Modified IEEE AC5A alternator-supplied rectifier excitation system with
    different minimum controller output.
    """
    def __init__(self) -> None:
        pass
        self.a: Optional[float] = 0.0  # Coefficient to allow different usage of the model (a).  Typical Value = 1.
        self.efd1: Optional[float] = 0.0  # Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 5.6
        self.efd2: Optional[float] = 0.0  # Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 4.2
        self.ka: Optional[float] = 0.0  # Voltage regulator gain (Ka).  Typical Value = 400.
        self.ke: Optional[float] = 0.0  # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
        self.kf: Optional[float] = 0.0  # Excitation control system stabilizer gains (Kf).  Typical Value = 0.03
        self.ks: Optional[float] = 0.0  # Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
        self.seefd1: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, Efd1 (S_E[Efd1]).  Typical Value = 0.86.
        self.seefd2: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, Efd2 (S_E[Efd2]).  Typical Value = 0.5.
        self.ta: Optional[float] = 0.0  # Voltage regulator time constant (Ta).  Typical Value = 0.02.
        self.tb: Optional[float] = 0.0  # Voltage regulator time constant (Tb).  Typical Value = 0.
        self.tc: Optional[float] = 0.0  # Voltage regulator time constant (Tc).  Typical Value = 0.
        self.te: Optional[float] = 0.0  # Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.8.
        self.tf1: Optional[float] = 0.0  # Excitation control system stabilizer time constant (Tf1).  Typical Value = 1.
        self.tf2: Optional[float] = 0.0  # Excitation control system stabilizer time constant (Tf2).  Typical Value = 0.8.
        self.tf3: Optional[float] = 0.0  # Excitation control system stabilizer time constant (Tf3).  Typical Value = 0.
        self.vrmax: Optional[float] = 0.0  # Maximum voltage regulator output (Vrmax).  Typical Value = 7.3.
        self.vrmin: Optional[float] = 0.0  # Minimum voltage regulator output (Vrmin).  Typical Value = -7.3.

