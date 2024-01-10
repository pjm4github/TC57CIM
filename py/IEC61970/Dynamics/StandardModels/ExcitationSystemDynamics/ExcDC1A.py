# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds


class ExcDC1A:
    """Modified IEEE DC1A direct current commutator exciter with speed input and
    without underexcitation limiters (UEL) inputs.
    """

    def __init__(self) -> None:
        super().__init__()
        self.edfmax: float = 0.0  # Maximum voltage exciter output limiter (Efdmax).
        self.efd1: float = 1.0  # Exciter voltage at which exciter saturation is defined (Efd1).
        self.efd2: float = 1.0  # Exciter voltage at which exciter saturation is defined (Efd2).
        self.efdmin: float = 0.0  # Minimum voltage exciter output limiter (Efdmin).
        self.exclim: bool  # (exclim). IEEE standard is ambiguous about lower limit on exciter output.
        self.ka: float = 1.0  # Voltage regulator gain (Ka).
        self.ke: float = 1.0  # Exciter constant related to self-excited field (Ke).
        self.kf: float = 1.0  # Excitation control system stabilizer gain (Kf).
        self.ks: float = 1.0  # Coefficient to allow different usage of the model-speed coefficient (Ks).
        self.seefd1: Optional[
            float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd1]).
        self.seefd2: Optional[
            float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd2]).
        self.ta: Seconds = Seconds()  # Voltage regulator time constant (Ta).
        self.tb: Seconds = Seconds()  # Voltage regulator time constant (Tb).
        self.tc: Seconds = Seconds()  # Voltage regulator time constant (Tc).
        self.te: Seconds = Seconds()  # Exciter time constant, integration rate associated with exciter control (Te).
        self.tf: Seconds = Seconds()  # Excitation control system stabilizer time constant (Tf).
        self.vrmax: float = 1.0  # Maximum voltage regulator output (Vrmax).
        self.vrmin: float = 1.0  # Minimum voltage regulator output (Vrmin).
