# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow


class ProtectionEquipmentInfo(AssetInfo):
    """
    Properties of protection equipment asset.
    @created 29-Dec-2023 6:23:04 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ground_trip: CurrentFlow = CurrentFlow()
        """Actual ground trip for this type of relay, if applicable."""
        self.phase_trip: CurrentFlow = CurrentFlow()
        """Actual phase trip for this type of relay, if applicable."""
