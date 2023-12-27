# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.Specimen import Specimen
from IEC61970.Base.Domain.Temperature import Temperature


class OilSpecimen(Specimen):

    def __init__(self):
        super().__init__()
        self.oil_sample_taken_from = None
        self.oil_sample_temperature = Temperature()
        self.oil_temperature_source = None
        self.sample_container = None
