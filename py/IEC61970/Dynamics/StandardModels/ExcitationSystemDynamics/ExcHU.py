# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcHu(ExcitationSystemDynamics):
    """
    Hungarian Excitation System Model, with built-in voltage transducer.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Major loop PI tag gain factor (Ae). Typical Value = 3.
        """
        super().__init__()
        self.ae: float = 1.0

        """
        Minor loop PI tag gain factor (Ai). Typical Value = 22.
        """
        self.ai: float = 1.0

        """
        AVR constant (Atr). Typical Value = 2.19.
        """
        self.atr: float = 1.0

        """
        Field voltage control signal upper limit on AVR base (Emax). Typical Value = 0.996.
        """
        self.emax: float = 1.0

        """
        Field voltage control signal lower limit on AVR base (Emin). Typical Value = -0.866.
        """
        self.emin: float = 1.0

        """
        Major loop PI tag output signal upper limit (Imax). Typical Value = 2.19.
        """
        self.imax: float = 1.0

        """
        Major loop PI tag output signal lower limit (Imin). Typical Value = 0.1.
        """
        self.imin: float = 1.0

        """
        Voltage base conversion constant (Ke). Typical Value = 4.666.
        """
        self.ke: float = 1.0

        """
        Current base conversion constant (Ki). Typical Value = 0.21428.
        """
        self.ki: float = 1.0

        """
        Major loop PI tag integration time constant (Te). Typical Value = 0.154.
        """
        self.te: Seconds = Seconds(1.0)

        """
        Minor loop PI control tag integration time constant (Ti). Typical Value = 0.01333.
        """
        self.ti: Seconds = Seconds(1.0)

        """
        Filter time constant (Tr). If a voltage compensator is used in conjunction with
        this excitation system model, Tr should be set to 0. Typical Value = 0.01.
        """
        self.tr: Seconds = Seconds(1.0)
