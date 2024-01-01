# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Optional

from IEC61968.InfIEC61968.InfAssetInfo.OldSwitchInfo import OldSwitchInfo
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow


class RecloserInfo(OldSwitchInfo):
    """
    Properties of recloser assets.
    @created 29-Dec-2023 6:23:14 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ground_trip_capableOptional[bool] = True
        """
        True if device has ground trip capability.
        """

        self.ground_trip_normal_enabledOptional[bool] = True
        """
        True if normal status of ground trip is enabled.
        """

        self.ground_trip_ratingOptional[CurrentFlow] = CurrentFlow()
        """
        Ground trip rating.
        """

        self.phase_trip_ratingOptional[CurrentFlow] = CurrentFlow()
        """
        Phase trip rating.
        """

        self.reclose_lockout_countOptional[int] = 0
        """
        Total number of phase reclose operations.
        """
