from IEC61970.InfIEC61970.InfPart303.ModelOperations.ModelOperationArg import ModelOperationArg
from IEC61970.Part303.GenericDataset.InstanceSet import InstanceSet


class DatasetArg(ModelOperationArg):
    """
    A model operation argument referencing a dataset instance.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:31:55 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.operation_dataset_arg_description = None  # Placeholder for DatasetArgDescription
        self.dataset = InstanceSet()  # Dataset referenced by this argument of a model operation
        # Assuming InstanceSet and ModelOperationArg are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
