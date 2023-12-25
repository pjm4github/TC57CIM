# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TapChanger import TapChanger


class TapSchedule:
    """
    A pre-established pattern over time for a tap step.
    @author pmora
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self):
        self.tap_changer = TapChanger()  # A TapSchedule is associated with a TapChanger

    def get_tap_changer(self) -> TapChanger:
        return self.tap_changer

    def set_tap_changer(self, new_val: TapChanger) -> None:
        self.tap_changer = new_val
