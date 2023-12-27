# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.AssetMeas.AssetAnalog import AssetAnalog
from IEC61968.AssetMeas.InspectionAnalogKind import InspectionAnalogKind


class InspectionAnalog(AssetAnalog):
    def __init__(self):
        super().__init__()
        self.kind = InspectionAnalogKind.AIR_PRESSURE_READING
        
