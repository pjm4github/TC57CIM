# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# from IEC61970.Base.Core.identified_object import IdentifiedObject
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.Environmental.EnvironmentalDataAuthority import EnvironmentalDataAuthority


class AlertTypeList(IdentifiedObject):
    """
    A named list of alert types.

    Note: the name of the list is reflected in the .name attribute (inherited from IdentifiedObject).
    @author ppbr003
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.version = ""
        # The environmental data authority responsible for publishing this list of alert types.
        self.environmental_data_authority = EnvironmentalDataAuthority()
