# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.AssetInfo.TransformerEndInfo import TransformerEndInfo
from IEC61968.AssetInfo.TransformerTest import TransformerTest
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.Voltage import Voltage


class OpenCircuitTest(TransformerTest):
    
    def __init__(self):
        super().__init__()
        self.energised_end_step = 0
        self.energised_end_voltage = Voltage()
        self.open_end_step = 0
        self.open_end_voltage = Voltage()
        self.phase_shift = AngleDegrees()
        self.open_end = TransformerEndInfo()
        self.energised_end = TransformerEndInfo()
