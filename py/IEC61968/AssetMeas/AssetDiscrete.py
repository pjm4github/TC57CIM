# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.TestStandard import TestStandard
from IEC61970.Base.Meas.Discrete import Discrete


class AssetDiscrete(Discrete):
    
    def __init__(self):
        super().__init__()
        self.test_standard = TestStandard()
