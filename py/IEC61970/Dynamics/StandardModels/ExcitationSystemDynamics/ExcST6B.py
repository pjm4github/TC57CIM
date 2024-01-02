# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcST6BOELselectorKind import ExcST6BOELselectorKind
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSt6B(ExcitationSystemDynamics):
    """
    Modified IEEE ST6B static excitation system with PID controller and optional
    inner feedbacks loop.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        # Excitation source reactance (Xc).  Typical Value = 0.05
        self.xc: float = 0.05

        # Exciter output current limit reference (Ilr).  Typical Value = 4.164
        self.ilr: float = 4.164

        # Selector (K1).
        # true = feedback is from Ifd
        # false = feedback is not from Ifd.
        # Typical Value = True.
        self.k1: bool = True

        # Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577
        self.kcl: float = 1.0577

        # Pre-control gain constant of the inner loop field regulator (Kff).  Typical
        # Value = 1.
        self.kff: float = 1.0

        # Feedback gain constant of the inner loop field regulator (Kg).  Typical
        # Value = 1.
        self.kg: float = 1.0

        # Voltage regulator integral gain (Kia).  Typical Value = 45.094.
        self.kia: float = 45.094

        # Exciter output current limit adjustment (Kcl).  Typical Value = 17.33.
        self.klr: float = 17.33

        # Forward gain constant of the inner loop field regulator (Km).  Typical Value = 1.
        self.km: float = 1.0

        # Voltage regulator proportional gain (Kpa).  Typical Value = 18.038.
        self.kpa: float = 18.038

        # Voltage regulator derivative gain (Kvd).  Typical Value = 0.
        self.kvd: float = 0.0

        # OEL input selector (OELin). Typical Value = noOELinput.
        self.oelin: Optional[ExcST6BOELselectorKind] = ExcST6BOELselectorKind.NO_OEL_INPUT

        # Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 0.02.
        self.tg: Seconds = Seconds(0.02)

        # Rectifier firing time constant (Ts).  Typical Value = 0.
        self.ts: Seconds = Seconds(0.0)

        # Voltage regulator derivative gain (Tvd).  Typical Value = 0.
        self.tvd: Seconds = Seconds(0.0)

        # Maximum voltage regulator output (Vamax).  Typical Value = 4.81.
        self.vamax: float = 4.81

        # Minimum voltage regulator output (Vamin).  Typical Value = -3.85.
        self.vamin: float = -3.85

        # Selector (Vilim).
        # true = Vimin-Vimax limiter is active
        # false = Vimin-Vimax limiter is not active.
        # Typical Value = true.
        self.vilim: bool = True

        # Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
        self.vimax: float = 10

        # Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
        self.vimin: float = -10.

        # Selector (Vmult).
        # true = multiply regulator output by terminal voltage
        # false = do not multiply regulator output by terminal voltage.
        # Typical Value = true.
        self.vmult: bool = True

        # Maximum voltage regulator output (Vrmax).  Typical Value = 4.81.
        self.vrmax: float = 4.81

        # Minimum voltage regulator output (Vrmin).  Typical Value = -3.85.
        self.vrmin: float =3.85
