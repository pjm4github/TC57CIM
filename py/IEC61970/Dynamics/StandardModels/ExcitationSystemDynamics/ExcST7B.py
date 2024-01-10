# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Union, Any

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcST7BOELselectorKind import ExcST7BOELselectorKind
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcST7BUELselectorKind import ExcST7BUELselectorKind


class ExcSt7B:
    """Modified IEEE ST7B static excitation system without stator current limiter (SCL) and current compensator (
    DROOP) inputs."""

    def __init__(self) -> None:
        """Constructor"""
        self.kh: Union[float, Any] = 1  # High-value gate feedback gain (Kh). Typical Value = 1
        self.kia: Union[float, Any] = 1  # Voltage regulator integral gain (Kia). Typical Value = 1
        self.kl: Union[float, Any] = 1  # Low-value gate feedback gain (Kl). Typical Value = 1
        self.kpa: Union[float, Any] = 40  # Voltage regulator proportional gain (Kpa). Typical Value = 40
        self.oelin: ExcST7BOELselectorKind = ExcST7BOELselectorKind.NO_OEL_INPUT  # OEL input selector (OELin).
        # Typical Value = noOELinput
        self.tb: Union[float, Any] = 1  # Regulator lag time constant (Tb). Typical Value = 1
        self.tc: Union[float, Any] = 1  # Regulator lead time constant (Tc). Typical Value = 1
        self.tf: Union[float, Any] = 1  # Excitation control system stabilizer time constant (Tf). Typical Value = 1
        self.tg: Union[
            float, Any] = 1  # Feedback time constant of inner loop field voltage regulator (Tg). Typical Value = 1
        self.tia: Union[float, Any] = 3  # Feedback time constant (Tia). Typical Value = 3
        self.ts: Union[float, Any] = 0  # Rectifier firing time constant (Ts). Typical Value = 0
        self.uelin: ExcST7BUELselectorKind = ExcST7BUELselectorKind.NO_UEL_INPUT  # UEL input selector (UELin).
        # Typical Value = noUELinput
        self.vmax: Union[float, Any] = 1.1  # Maximum voltage reference signal (Vmax). Typical Value = 1.1
        self.vmin: Union[float, Any] = 0.9  # Minimum voltage reference signal (Vmin). Typical Value = 0.9
        self.vrmax: Union[float, Any] = 5  # Maximum voltage regulator output (Vrmax). Typical Value = 5
        self.vrmin: Union[float, Any] = -4.5  # Minimum voltage regulator output (Vrmin). Typical Value = -4.5
