from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.ModelOperations.ModelOperationDescription import ModelOperationDescription


class ModelOperationArgDescription(IdentifiedObject):
    """
    The type of custom operation dataset role for an operation description.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.multiplicity_maximum = int()  # Maximum multiplicity of instance arguments for a single operation (-1 for unlimited)
        self.multiplicity_minimum = int()  # Minimum multiplicity of instance arguments for a single operation (0 for optional)
        self.model_operation_definition = ModelOperationDescription()  # Placeholder for the associated ModelOperationDescription
        # Assuming ModelOperationDescription is a previously defined class
        # If ModelOperationDescription is not defined, this will raise an error and needs to be implemented
