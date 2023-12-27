from IEC61968.Assets.TestStandard import TestStandard
from IEC61970.Base.Meas.StringMeasurement import StringMeasurement


class AssetStringMeasurement(StringMeasurement):
    
    def __init__(self):
        super().__init__()
        self.kind = None
        self.test_standard = TestStandard()
