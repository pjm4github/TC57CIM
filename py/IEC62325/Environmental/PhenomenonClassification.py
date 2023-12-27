# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# import local modules
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.Environmental.EnvironmentalDataAuthority import EnvironmentalDataAuthority


class PhenomenonClassification(IdentifiedObject):
    """
    A pre-defined phenomenon classification as defined by a particular authority.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        """
        Constructor
        """
        self.environmental_data_authority = EnvironmentalDataAuthority()
