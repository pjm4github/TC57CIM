# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.TestStandard import TestStandard
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Base.Meas.Analog import Analog


class AssetAnalog(Analog):
    def __init__(self):
        super().__init__()
        self.detection_limit = 0.0
        self.precision = 0.0
        self.reporting_temperature = Temperature()
        self.test_standard = TestStandard()
