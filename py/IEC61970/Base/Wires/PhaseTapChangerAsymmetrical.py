# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear


class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """
    Describes the tap model for an asymmetrical phase shifting transformer in which
    the difference voltage vector adds to the primary side voltage. The angle
    between the primary side voltage and the difference voltage is named the
    winding connection angle. The phase shift depends on both the difference
    voltage magnitude and the winding connection angle.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self):
        super().__init__()
        self.winding_connection_angle = AngleDegrees()

    def get_winding_connection_angle(self) -> AngleDegrees:
        return self.winding_connection_angle

    def set_winding_connection_angle(self, new_val: AngleDegrees):
        self.winding_connection_angle = new_val
