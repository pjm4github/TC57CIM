# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.AssetAnalog import AssetAnalog
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.OilAnalysisPaperAnalogKind import OilAnalysisPaperAnalogKind


class OilAnalysisPaperAnalog(AssetAnalog):

    def __init__(self):
        super().__init__()

        # Kind of analog representing oil paper degradation analysis result.
        self.kind = OilAnalysisPaperAnalogKind.ACF
