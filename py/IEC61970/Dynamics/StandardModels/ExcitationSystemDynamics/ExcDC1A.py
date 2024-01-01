# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional, TypedDict


class ExcDC1A(TypedDict):
    """Modified IEEE DC1A direct current commutator exciter with speed input and
    without underexcitation limiters (UEL) inputs.
    """

    def __init__(self) -> None:
        super().__init__()
        self.edfmax: Optional[float] = 0.0  # Maximum voltage exciter output limiter (Efdmax).
        self.efd1: Optional[float] = 1.0  # Exciter voltage at which exciter saturation is defined (Efd1).
        self.efd2: Optional[float] = 1.0  # Exciter voltage at which exciter saturation is defined (Efd2).
        self.efdmin: Optional[float] = 0.0  # Minimum voltage exciter output limiter (Efdmin).
        self.exclim: Optional[bool]  # (exclim). IEEE standard is ambiguous about lower limit on exciter output.
        self.ka: Optional[float] = 1.0  # Voltage regulator gain (Ka).
        self.ke: Optional[float] = 1.0  # Exciter constant related to self-excited field (Ke).
        self.kf: Optional[float] = 1.0  # Excitation control system stabilizer gain (Kf).
        self.ks: Optional[float] = 1.0  # Coefficient to allow different usage of the model-speed coefficient (Ks).
        self.seefd1: Optional[
            float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd1]).
        self.seefd2: Optional[
            float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd2]).
        self.ta: Optional[float] = 1.0  # Voltage regulator time constant (Ta).
        self.tb: Optional[float] = 1.0  # Voltage regulator time constant (Tb).
        self.tc: Optional[float] = 1.0  # Voltage regulator time constant (Tc).
        self.te: Optional[float] = 1.0  # Exciter time constant, integration rate associated with exciter control (Te).
        self.tf: Optional[float] = 1.0  # Excitation control system stabilizer time constant (Tf).
        self.vrmax: Optional[float] = 1.0  # Maximum voltage regulator output (Vrmax).
        self.vrmin: Optional[float] = 1.0  # Minimum voltage regulator output (Vrmin).
