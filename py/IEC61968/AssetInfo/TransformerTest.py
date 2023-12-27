# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.ApparentPower import ApparentPower
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Base.Core import IdentifiedObject

class TransformerTest(IdentifiedObject):
    
    def __init__(self):
        self.base_power = ApparentPower()
        self.temperature = Temperature()
