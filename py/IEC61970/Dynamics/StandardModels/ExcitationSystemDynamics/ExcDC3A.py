# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDc3A(ExcitationSystemDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.edf_max: float = 1.0  # Maximum voltage exciter output limiter (Efdmax). Typical Value = 99.
        self.efd1: float = 1.0  # Exciter voltage at which exciter saturation is defined (Efd1). Typical Value = 2.6.
        self.efd2: float = 1.0  # Exciter voltage at which exciter saturation is defined (Efd2). Typical Value = 3.45.
        self.efdlim: bool = False  # (Efdlim). true = exciter output limiter is active, false = exciter output
        # limiter not active. Typical Value = true.
        self.efdmin: float = 1.0  # Minimum voltage exciter output limiter (Efdmin). Typical Value = -99.
        self.exclim: bool = False  # (exclim). IEEE standard is ambiguous about lower limit on exciter output,
        # true = a lower limit of zero is applied to integrator output, false = a lower limit of zero not applied to
        # integrator output. Typical Value = true.
        self.ke: float = 1.0  # Exciter constant related to self-excited field (Ke). Typical Value = 1.
        self.kr: float = 1.0  # Death band (Kr). If Kr is not zero, the voltage regulator input changes at a constant
        # rate if Verr > Kr or Verr < -Kr as per the IEEE (1968) Type 4 model. If Kr is zero, the error signal drives
        # the voltage regulator continuously as per the IEEE (1980) DC3 and IEEE (1992, 2005) DC3A models. Typical
        # Value = 0.
        self.ks: float = 1.0  # Coefficient to allow different usage of the model-speed coefficient (Ks). Typical
        # Value = 0.
        self.kv: float = 1.0  # Fast raise/lower contact setting (Kv). Typical Value = 0.05.
        self.seefd1: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
        # Efd1 (Se[Efd1]). Typical Value = 0.1.
        self.seefd2: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
        # Efd2 (Se[Efd2]). Typical Value = 0.35.
        self.te: Seconds = Seconds()  # Exciter time constant, integration rate associated with exciter control (Te).
        # Typical Value = 1.83.
        self.trh: Seconds = Seconds()  # Rheostat travel time (Trh). Typical Value = 20.
        self.vrmax: float = 1.0  # Maximum voltage regulator output (Vrmax). Typical Value = 5.
        self.vrmin: float = 1.0  # Minimum voltage regulator output (Vrmin). Typical Value = 0.
