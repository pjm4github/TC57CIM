# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61968.InfIEC61968.InfAssetInfo.FaultIndicatorResetKind import FaultIndicatorResetKind


class FaultIndicatorInfo(AssetInfo):
    """
    Parameters of fault indicator asset.
    @created 29-Dec-2023 6:22:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.reset_kind: FaultIndicatorResetKind = FaultIndicatorResetKind.REMOTE
