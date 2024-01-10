# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.MSSZone import MSSZone


class MeteredSubSystem(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.mss_zone = MSSZone()
