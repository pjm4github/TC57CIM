# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource


# An area of activity defined within the energy market.
# @author effantin-cyr
# @version 1.0
# @created 25-dec-2023 9:21:22 PM
class Domain(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.registered_resource = RegisteredResource()
