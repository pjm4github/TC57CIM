# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from IEC61968.InfIEC61968.InfAssetInfo.OldSwitchInfo import OldSwitchInfo
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow


class BreakerInfo(OldSwitchInfo):
    """
    Properties of breaker assets.
    @created 29-Dec-2023 6:21:42 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.phase_trip: CurrentFlow()
