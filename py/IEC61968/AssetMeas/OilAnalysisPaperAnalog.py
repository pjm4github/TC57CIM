# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.AssetMeas.AssetAnalog import AssetAnalog
from IEC61968.AssetMeas.OilAnalysisPaperAnalogKind import OilAnalysisPaperAnalogKind


class OilAnalysisPaperAnalog(AssetAnalog):

    def __init__(self):
        super().__init__()

        # Kind of analog representing oil paper degradation analysis result.
        self.kind = OilAnalysisPaperAnalogKind.ETHANOL
