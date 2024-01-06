from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Part552Header.URI import URI


class Model:
    """
    Author: selaost1
    Version: 1.0
    Created: 29-Dec-2023 10:49:20 PM
    """
    def __init__(self):
        self.created = DateTime()  # Creation time of the model
        self.description = str()  # Description of the model
        self.modeling_authority_set = URI()  # Modeling authority set URI
        self.profile = URI()  # Profile URI
        self.scenario_time = DateTime()  # Scenario time for the model
        self.version = int()  # Version of the model
        self.supersedes = Model()  # Model that this model supersedes
        self.dependent_on = Model()  # Model that this model is dependent on
