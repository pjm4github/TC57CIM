# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ForbiddenRegion(IdentifiedObject):
    """
    Forbidden region is operating ranges where the units are unable to maintain
    steady operation without causing equipment damage. The four attributes that
    define a forbidden region are the low MW, the High MW, the crossing time, and
    the crossing cost.
    
    @created 28-Dec-2023 12:13:58 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.crossing_costfloat = 0.0
        """Cost associated with crossing the forbidden region"""

        self.cross_timeOptional[int] = 0
        """Time to cross the forbidden region in minutes."""

        self.high_mwfloat = 0.0
        """High end of the region definition"""

        self.low_mwfloat = 0.0
        """Low end of the region definition."""
