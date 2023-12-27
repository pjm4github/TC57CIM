# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.Voltage import Voltage
from IEC61968.Assets.AssetInfo import AssetInfo

class BusbarSectionInfo(AssetInfo):
    
    def __init__(self):
        super().__init__()
        self.rated_current = CurrentFlow()
        self.rated_voltage = Voltage()
