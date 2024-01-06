from IEC61970.Part303.GenericDataset.InstanceSet import InstanceSet


class ModelPartVersion:
    """
    Versioned instance of a model part.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        self.model_part = ModelPartVersion()  # Model part of the model part version
        self.full_model_dataset = InstanceSet()  # Dataset of the model part version
        # Assuming ModelPartVersion and InstanceSet are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
