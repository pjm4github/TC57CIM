from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectChangeVersion import \
    NetworkModelProjectChangeVersion
from IEC61970.Part552Header.ModelDescription.Model import Model
from IEC61970.Part552Header.Statements import Statements


class DifferenceModel(Model):
    """
    Author: selaost1
    Version: 1.0
    Created: 29-Dec-2023 10:48:23 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.reverse_differences = Statements()  # Reverse differences in the model
        self.forward_differences = Statements()  # Forward differences in the model
        self.network_model_project_change_version = NetworkModelProjectChangeVersion()  # Associated NetworkModelProjectChangeVersion
