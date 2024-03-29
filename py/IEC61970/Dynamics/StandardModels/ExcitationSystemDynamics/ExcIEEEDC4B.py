# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeDc4B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC4B model. These excitation
    systems utilize a field-controlled dc commutator exciter with a continuously
    acting voltage regulator having supplies obtained from the generator or
    auxiliary bus. Reference: IEEE Standard 421.5-2005 Section 5.4.
    """

    def __init__(self) -> None:
        # Exciter voltage at which exciter saturation is defined (E_fd1). Typical Value = 1.75.
        super().__init__()
        self.efd1: float = 1.0

        # Exciter voltage at which exciter saturation is defined (E_fd2). Typical Value = 2.33.
        self.efd2: float = 1.0

        # Voltage regulator gain (K_A). Typical Value = 1.
        self.ka: float = 1.0

        # Regulator derivative gain (K_D). Typical Value = 20.
        self.kd: float = 1.0

        # Exciter constant related to self-excited field (K_E). Typical Value = 1.
        self.ke: float = 1.0

        # Excitation control system stabilizer gain (K_F). Typical Value = 0.
        self.kf: float = 1.0

        # Regulator integral gain (K_I). Typical Value = 20.
        self.ki: float = 1.0

        # Regulator proportional gain (K_P). Typical Value = 20.
        self.kp: float = 1.0

        # OEL input (OELin). true = LV gate, false = subtract from error signal. Typical Value = true.
        self.oelin: bool = False

        # Exciter saturation function value at the corresponding exciter voltage  E_fd1 (S_E[E_fd1]). Typical Value = 0.08.
        self.seefd1: float = 1.0

        # Exciter saturation function value at the corresponding exciter voltage  E_fd2 (S_E[E_fd2]). Typical Value = 0.27.
        self.seefd2: float = 1.0

        # Voltage regulator time constant (T_A).  Typical Value = 0.2.
        self.ta: Seconds = Seconds(1.0)

        # Regulator derivative filter time constant(T_D). Typical Value = 0.01.
        self.td: Seconds = Seconds(1.0)

        # Exciter time constant, integration rate associated with exciter control (T_E). Typical Value = 0.8.
        self.te: Seconds = Seconds(1.0)

        # Excitation control system stabilizer time constant (T_F). Typical Value = 1.
        self.tf: float = 1.0

        # UEL input (UELin). true = HV gate false = add to error signal. Typical Value = true.
        self.uelin: bool = False

        # Minimum exciter voltage output(V_EMIN).  Typical Value = 0.
        self.vemin: float = 1.0

        # Maximum voltage regulator output (V_RMAX).  Typical Value = 2.7.
        self.vrmax: float = 1.0

        # Minimum voltage regulator output (V_RMIN).  Typical Value = -0.9.
        self.vrmin: float = 1.0
