# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDc2A(ExcitationSystemDynamics):
    """
    Modified IEEE DC2A direct current commutator exciters with speed input, one more leg block in feedback loop
    and without underexcitation limiters (UEL) inputs. DC type 2 excitation system model with added speed multiplier,
    added lead-lag, and voltage-dependent limits.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.efd1: float = 1.0  # Exciter voltage at which exciter saturation is defined (Efd1). Typical Value = 3.05.
        self.efd2: float = 1.0  # Exciter voltage at which exciter saturation is defined (Efd2). Typical Value = 2.29.
        self.exclim: bool = False  # (exclim). IEEE standard is ambiguous about lower limit on exciter output.
        # True = a lower limit of zero is applied to integrator output
        # False = a lower limit of zero is not applied to integrator output. Typical Value = True.
        self.ka: float = 1.0  # Voltage regulator gain (Ka). Typical Value = 300.
        self.ke: float = 1.0  # Exciter constant related to self-excited field (Ke).
        # If Ke is entered as zero, the model calculates an effective value of Ke such that the initial condition
        # value of Vr is zero. The zero value of Ke is not changed. If Ke is entered as non-zero, its value is used
        # directly, without change. Typical Value = 1.
        self.kf: float = 1.0  # Excitation control system stabilizer gain (Kf). Typical Value = 0.1.
        self.ks: float = 1.0  # Coefficient to allow different usage of the model-speed coefficient (Ks). Typical
        # Value = 0.
        self.seefd1: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
        # Efd1 (Se[Efd1]). Typical Value = 0.279.
        self.seefd2: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
        # Efd2 (Se[Efd2]). Typical Value = 0.117.
        self.ta: Seconds = Seconds()  # Voltage regulator time constant (Ta). Typical Value = 0.01.
        self.tb: Seconds = Seconds()  # Voltage regulator time constant (Tb). Typical Value = 0.
        self.tc: Seconds = Seconds()  # Voltage regulator time constant (Tc). Typical Value = 0.
        self.te: Seconds = Seconds()  # Exciter time constant, integration rate associated with exciter control (Te).
        # Typical Value = 1.33.
        self.tf: Seconds = Seconds()  # Excitation control system stabilizer time constant (Tf). Typical Value = 0.675.
        self.tf1: Seconds = Seconds()  # Excitation control system stabilizer time constant (Tf1). Typical Value = 0.
        self.vrmax: float = 1.0  # Maximum voltage regulator output (Vrmax). Typical Value = 4.95.
        self.vrmin: float = 1.0  # Minimum voltage regulator output (Vrmin). Typical Value = -4.9.
        self.vtlim: bool = False  # (Vtlim). True = limiter at the block [Ka/(1+sTa)] is dependent on Vt
        # False = limiter at the block is not dependent on Vt. Typical Value = True.
