# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.AssetAnalog import AssetAnalog


class OilAnalysisFluidAnalog(AssetAnalog):
    """
    Asset oil analysis fluid test type of analog.
    @author ppbr003
    @version 1.0
    @created 20-Dec-2023 10:57:27 AM
    """
    
    def __init__(self):
        """
        Kind of analog representing oil fluid test analysis result.
        """
        super().__init__()
        self.kind = None
