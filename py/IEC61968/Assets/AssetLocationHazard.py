# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Location import Location
from IEC61968.Common.Hazard import Hazard


class AssetLocationHazard(Hazard):

    def __init__(self):
        super().__init__()
        self.kind = None
        self.location = Location()
