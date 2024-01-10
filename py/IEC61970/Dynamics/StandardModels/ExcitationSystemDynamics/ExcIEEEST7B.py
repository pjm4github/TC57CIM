# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Union
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcST7BOELselectorKind import ExcST7BOELselectorKind
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcST7BUELselectorKind import ExcST7BUELselectorKind


class ExcIEEEST7B:
    """
    The class represents IEEE Std 421.5-2005 type ST7B model. This model is
    representative of static potential-source excitation systems. In this system,
    the AVR consists of a PI voltage regulator. A phase lead-lag filter in series
    allows introduction of a derivative function, typically used with brushless
    excitation systems. In that case, the regulator is of the PID type. In addition,
    the terminal voltage channel includes a phase lead-lag filter. The AVR
    includes the appropriate inputs on its reference for overexcitation limiter
    (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and
    current compensator (DROOP). All these limitations, when they work at voltage
    reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in
    operation. However, the UEL limitation can also be transferred to the high
    value (HV) gate acting on the output signal. In addition, the output signal
    passes through a low value (LV) gate for a ceiling overexcitation limiter
    (OEL2).
    Reference: IEEE Standard 421.5-2005 Section 7.7
    """

    def __init__(self) -> None:
        # High-value gate feedback gain (K_H). Typical Value 1.
        self.kh: Union[float, int] = 1

        # Voltage regulator integral gain (K_IA). Typical Value = 1.
        self.kia: Union[float, int] = 1

        # Low-value gate feedback gain (K_L). Typical Value 1.
        self.kl: Union[float, int] = 1

        # Voltage regulator proportional gain (K_PA). Typical Value = 40.
        self.kpa: Union[float, int] = 40

        # OEL input selector (OELin). Typical Value = noOELinput.
        self.oelin: ExcST7BOELselectorKind = ExcST7BOELselectorKind.NO_OEL_INPUT

        # Regulator lag time constant (T_B). Typical Value 1.
        self.tb: Seconds = Seconds(1)

        # Regulator lead time constant (T_C). Typical Value 1.
        self.tc: Seconds = Seconds(1)

        # Excitation control system stabilizer time constant (T_F). Typical Value 1.
        self.tf: Seconds = Seconds(1)

        """
        Feedback time constant of inner loop field voltage regulator (T_G).
        Typical Value 1.
        """
        self.tg: Seconds = Seconds(1)

        # Feedback time constant (T_IA). Typical Value = 3.
        self.tia: Seconds = Seconds(3)

        # UEL input selector (UELin). Typical Value = noUELinput.
        self.uelin: ExcST7BUELselectorKind = ExcST7BUELselectorKind.NO_UEL_INPUT

        # Maximum voltage reference signal (V_MAX). Typical Value = 1.1.
        self.vmax: Union[float, int] = 1.1

        # Minimum voltage reference signal (V_MIN). Typical Value = 0.9.
        self.vmin: Union[float, int] = 0.9

        # Maximum voltage regulator output (V_RMAX). Typical Value = 5.
        self.vrmax: Union[float, int] = 5

        # Minimum voltage regulator output (V_RMIN). Typical Value = -4.5.
        self.vrmin: Union[float, int] = -4.5

