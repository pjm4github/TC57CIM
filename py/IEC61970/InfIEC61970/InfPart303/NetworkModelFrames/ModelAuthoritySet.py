# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:55:15 2024
# A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.
# This class is typically not included in instance data exchange as this information is tracked by other mechanisms in the exchange.
# @created 02-Jan-2024 9:22:40 PM
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.ModelAuthority import ModelAuthority


class ModelAuthoritySet(IdentifiedObject):

    # A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
    def __init__(self):
        super().__init__()
        self.modeling_authority = ModelAuthority()  # initializing the modeling authority attribute with the ModelAuthority class
