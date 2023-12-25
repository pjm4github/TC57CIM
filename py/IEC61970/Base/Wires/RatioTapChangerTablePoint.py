# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RatioTapChangerTable import RatioTapChangerTable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TapChangerTablePoint import TapChangerTablePoint


class RatioTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the ratio tap changer tabular curve.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self):
        super().__init__()
        self.ratio_tap_changer_table = RatioTapChangerTable()

    def get_ratio_tap_changer_table(self) -> RatioTapChangerTable:
        return self.ratio_tap_changer_table

    def set_ratio_tap_changer_table(self, new_val: RatioTapChangerTable) -> None:
        self.ratio_tap_changer_table = new_val
