# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RatioTapChangerTable import RatioTapChangerTable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TapChanger import TapChanger
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TransformerControlMode import TransformerControlMode


class RatioTapChanger(TapChanger):
    """
    A tap changer that changes the voltage ratio impacting the voltage magnitude
    but not the phase angle across the transformer.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ratio_tap_changer_table = RatioTapChangerTable()
        self.step_voltage_increment = PerCent()
        self.transformer_control_mode = TransformerControlMode.VOLT

    def get_ratio_tap_changer_table(self) -> RatioTapChangerTable:
        return self.ratio_tap_changer_table

    def get_step_voltage_increment(self) -> PerCent:
        return self.step_voltage_increment

    def get_transformer_control_mode(self) -> TransformerControlMode:
        return self.transformer_control_mode

    def set_ratio_tap_changer_table(self, new_val: RatioTapChangerTable) -> None:
        self.ratio_tap_changer_table = new_val

    def set_step_voltage_increment(self, new_val: PerCent) -> None:
        self.step_voltage_increment = new_val

    def set_transformer_control_mode(self, new_val: TransformerControlMode) -> None:
        self.transformer_control_mode = new_val

