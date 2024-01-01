# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Any, Union
from datetime import datetime

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeSt6B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST6B model. This model consists
    of a PI voltage regulator with an inner loop field voltage regulator and pre-
    control. The field voltage regulator implements a proportional control. The pre-
    control and the delay in the feedback circuit increase the dynamic response. Reference:
    IEEE Standard 421.5-2005 Section 7.6
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
        """
        Exciter output current limit reference (I_LR).  Typical Value = 4.164.
        """
        self.ilr: Union[int, float]
        """
        Exciter output current limit adjustment (K_CI).  Typical Value = 1.0577.
        """
        self.kci: Union[int, float]
        """
        Pre-control gain constant of the inner loop field regulator (K_FF). Typical Value = 1.
        """
        self.kff: Union[int, float]
        """
        Feedback gain constant of the inner loop field regulator (K_G). Typical Value = 1.
        """
        self.kg: Union[int, float]
        """
        Voltage regulator integral gain (K_IA).  Typical Value = 45.094.
        """
        self.kia: Union[int, float]
        """
        Exciter output current limiter gain (K_LR).  Typical Value = 17.33.
        """
        self.klr: Union[int, float]
        """
        Forward gain constant of the inner loop field regulator (K_M). Typical Value = 1.
        """
        self.km: Union[int, float]
        """
        Voltage regulator proportional gain (K_PA).  Typical Value = 18.038.
        """
        self.kpa: Union[int, float]
        """
        OEL input selector (OELin). Typical Value = noOELinput
        """
        self.oelin: ExcSt6BOELselectorKind
        """
        Feedback time constant of inner loop field voltage regulator (T_G). Typical Value = 0.02.
        """
        self.tg: datetime
        """
        Maximum voltage regulator output (V_AMAX).  Typical Value = 4.81.
        """
        self.vamax: Union[int, float]
        """
        Minimum voltage regulator output (V_AMIN).  Typical Value = -3.85.
        """
        self.vamin: Union[int, float]
        """
        Maximum voltage regulator output (V_RMAX).  Typical Value = 4.81.
        """
        self.vrmax: Union[int, float]
        """
        Minimum voltage regulator output (V_RMIN).  Typical Value = -3.85.
        """
        self.vrmin: Union[int, float]
