# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Optional

from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61968.InfIEC61968.InfAssetInfo.CompositeSwitchKind import CompositeSwitchKind
from IEC61970.Base.Core.PhaseCode import PhaseCode
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.Voltage import Voltage


class CompositeSwitchInfo(AssetInfo):
    """
    Properties of a composite switch.
    @created 29-Dec-2023 6:21:55 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ganged: bool = False
        """
        True if multi-phase switch controls all phases concurrently.
        """

        self.init_op_mode: Optional[str] = ""
        """
        Initial operating mode, with the following values: Automatic, Manual.
        """

        self.interrupting_rating: Optional[CurrentFlow] = CurrentFlow()
        """
        Breaking capacity, or short circuit rating, is the maximum rated current
        which the device can safely interrupt at the rated voltage.
        """

        self.kind: Optional[CompositeSwitchKind] = CompositeSwitchKind.UG_MULTI_SWITCH
        """
        Kind of composite switch.
        """

        self.phase_code: Optional[PhaseCode] = PhaseCode.A
        """
        Phases carried, if applicable.
        """

        self.phase_count: Optional[int] = 0
        """
        Supported number of phases, typically 0, 1 or 3.
        """

        self.rated_voltage: Optional[Voltage] = Voltage()
        """
        Rated voltage.
        """

        self.remote: bool = True
        """
        True if device is capable of being operated by remote control.
        """

        self.switch_state_count: Optional[int] = 0
        """
        Number of switch states represented by the composite switch.
        """
