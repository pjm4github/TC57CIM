# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ConfigurationEvent import ConfigurationEvent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class OrganisationRole(IdentifiedObject):
    
    """Identifies a way in which an organisation may participate in the utility
    enterprise (e.g., customer, manufacturer, etc).
    """
    def __init__(self):
        super().__init__()
        self.configuration_events = None  # All configuration events created for this organisation role
        self.organisation = None
    # All configuration events created for this organisation role.
    ConfigurationEvents= ConfigurationEvent()

    # Organisation having this role.
    Organisation= Organisation()

  # Organisation having this role
