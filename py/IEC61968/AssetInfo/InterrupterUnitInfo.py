# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.AssetInfo.InterruptingMediumKind import InterruptingMediumKind
from IEC61968.Assets.AssetInfo import AssetInfo


class InterrupterUnitInfo(AssetInfo):

    def __init__(self):
        super().__init__()
        self.interrupting_medium = InterruptingMediumKind.AIR_BLAST
