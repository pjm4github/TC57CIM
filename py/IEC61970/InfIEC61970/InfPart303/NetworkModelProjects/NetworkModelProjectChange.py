from IEC61970.Base.Core import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectComponent import \
    NetworkModelProjectComponent


class NetworkModelProjectChange(IdentifiedObject):
    """
    Network model project change described by versions of an associated change set.
    Has persistent identity over multiple versions of the associated change set.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        # Assuming NetworkModelProjectComponent is a separate class that should be inherited or associated
        # If it's a typo and should not be there, remove the following line
        self.network_model_project_component = NetworkModelProjectComponent()  # Associated NetworkModelProjectComponent
