# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseTapChangerTabular import PhaseTapChangerTabular


class PhaseTapChangerTable:
    """
    Describes a tabular curve for how the phase angle difference and impedance
    varies with the tap step.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self):
        self.phase_tap_changer_tabular = PhaseTapChangerTabular()

    def get_phase_tap_changer_tabular(self) -> PhaseTapChangerTabular:
        return self.phase_tap_changer_tabular

    def set_phase_tap_changer_tabular(self, new_val: PhaseTapChangerTabular) -> None:
        self.phase_tap_changer_tabular = new_val
