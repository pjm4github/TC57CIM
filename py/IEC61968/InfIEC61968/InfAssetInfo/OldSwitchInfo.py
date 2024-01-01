# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Optional

from IEC61968.AssetInfo.SwitchInfo import SwitchInfo
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.Voltage import Voltage


class OldSwitchInfo(SwitchInfo):
    """
    Properties of switch assets.
    @created 29-Dec-2023 6:23:45 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.dielectric_strengthOptional[Voltage] = Voltage()
        """
        The maximum rms voltage that may be applied across an open contact without
        breaking down the dielectric properties of the switch in the open position.
        """

        self.load_breakOptional[bool] = False
        """
        True if switch has load breaking capability. Unless specified false, this is
        always assumed to be true for breakers and reclosers.
        """

        self.making_capacityOptional[CurrentFlow] = CurrentFlow()
        """
        The highest value of current the switch can make at the rated voltage under
        specified operating conditions without suffering significant deterioration of
        its performance.
        """

        self.minimum_currentOptional[CurrentFlow] = CurrentFlow()
        """
        The lowest value of current that the switch can make, carry and break in
        uninterrupted duty at the rated voltage under specified operating conditions
        without suffering significant deterioration of its performance.
        """

        self.pole_countOptional[int] = 0
        """
        Number of poles (i.e. of current carrying conductors that are switched).
        """

        self.remoteOptional[bool] = False
        """
        True if device is capable of being operated by remote control.
        """

        self.withstand_currentOptional[CurrentFlow] = CurrentFlow()
        """
        The highest value of current the switch can carry in the closed position at the
        rated voltage under specified operating conditions without suffering
        significant deterioration of its performance.
        """
