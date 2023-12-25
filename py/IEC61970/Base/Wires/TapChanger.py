# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TapChangerControl import TapChangerControl


class TapChanger:
    """
    Mechanism for changing transformer winding tap positions.
    @author pmora
    @created 15-Dec-2023 4:38:29 PM
    """
    def __init__(self) -> None:
        """
        Constructor of TapChanger class.
        """
        self.control_enabled: bool = False
        self.high_step: int = 0
        self.initial_delay: Optional[Seconds] = Seconds()
        self.low_step: int = 1
        self.ltc_flag: bool = True
        self.neutral_step: int = 0
        self.neutral_u: Optional[Voltage] = Voltage()
        self.normal_step: int = 1
        self.step: float = 1.0
        self.subsequent_delay: Optional[Seconds] = Seconds()
        self.tap_changer_control: Optional[TapChangerControl] = TapChangerControl()

    def get_control_enabled(self) -> bool:
        return self.control_enabled

    def get_high_step(self) -> int:
        return self.high_step

    def get_initial_delay(self) -> Seconds:
        return self.initial_delay

    def get_low_step(self) -> int:
        return self.low_step

    def get_ltc_flag(self) -> bool:
        return self.ltc_flag

    def get_neutral_step(self) -> int:
        return self.neutral_step

    def get_neutral_u(self) -> Voltage:
        return self.neutral_u

    def get_normal_step(self) -> int:
        return self.normal_step

    def get_step(self) -> float:
        return self.step

    def get_subsequent_delay(self) -> Seconds:
        return self.subsequent_delay

    def get_tap_changer_control(self) -> TapChangerControl:
        return self.tap_changer_control

    def set_control_enabled(self, new_val: bool) -> None:
        self.control_enabled = new_val

    def set_high_step(self, new_val: int) -> None:
        self.high_step = new_val

    def set_initial_delay(self, new_val: Seconds) -> None:
        self.initial_delay = new_val

    def set_low_step(self, new_val: int) -> None:
        self.low_step = new_val

    def set_ltc_flag(self, new_val: bool) -> None:
        self.ltc_flag = new_val

    def set_neutral_step(self, new_val: int) -> None:
        self.neutral_step = new_val

    def set_neutral_u(self, new_val: Voltage) -> None:
        self.neutral_u = new_val

    def set_normal_step(self, new_val: int) -> None:
        self.normal_step = new_val

    def set_step(self, new_val: float) -> None:
        self.step = new_val

    def set_subsequent_delay(self, new_val: Seconds) -> None:
        self.subsequent_delay = new_val

    def set_tap_changer_control(self, new_val: TapChangerControl) -> None:
        self.tap_changer_control = new_val
