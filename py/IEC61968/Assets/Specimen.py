# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.AssetTestSampleTaker import AssetTestSampleTaker
from IEC61970.Base.Domain.Temperature import Temperature
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Specimen(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.ambient_temperature_at_sampling = Temperature()
        self.humidity_at_sampling = PerCent()
        self.specimen_id = ""
        self.specimen_sample_date_time = DateTime()
        self.specimen_to_lab_date_time = DateTime()
        self.asset_test_sample_taker = AssetTestSampleTaker()
