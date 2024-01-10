# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.ConfigurationEvent import ConfigurationEvent
from IEC61968.Common.Organisation import Organisation
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class OrganisationRole(IdentifiedObject):
    
    """Identifies a way in which an organisation may participate in the utility
    enterprise (e.g., customer, manufacturer, etc).
    """
    def __init__(self):
        super().__init__()
        self.configuration_events = ConfigurationEvent()  # All configuration events created for this organisation role
        self.organisation = Organisation()
        # All configuration events created for this organisation role.

        # Organisation having this role.

