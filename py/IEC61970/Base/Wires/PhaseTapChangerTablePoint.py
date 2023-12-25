# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseTapChangerTable import PhaseTapChangerTable
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TapChangerTablePoint import TapChangerTablePoint


class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the phase tap changer tabular curve.
    @author pmora
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.angle = AngleDegrees()
        self.phase_tap_changer_table = PhaseTapChangerTable()

    def get_angle(self) -> AngleDegrees:
        """
        Get the angle
        @return: The angle difference in degrees
        """
        return self.angle

    def get_phase_tap_changer_table(self) -> PhaseTapChangerTable:
        """
        Get the phase tap changer table
        @return: The table of this point
        """
        return self.phase_tap_changer_table

    def set_angle(self, new_val: AngleDegrees) -> None:
        """
        Set the angle
        @param new_val: The new angle value
        """
        self.angle = new_val

    def set_phase_tap_changer_table(self, new_val: PhaseTapChangerTable) -> None:
        """
        Set the phase tap changer table
        @param new_val: The new phase tap changer table value
        """
        self.phase_tap_changer_table = new_val
