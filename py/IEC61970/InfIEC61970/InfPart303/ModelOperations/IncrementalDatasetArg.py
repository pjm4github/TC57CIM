from IEC61970.InfIEC61970.InfPart303.ModelOperations.ModelOperationArg import ModelOperationArg
from IEC61970.Part303.GenericDataset.ChangeSet import ChangeSet


class IncrementalDatasetArg(ModelOperationArg):
    """
    A generic model operation argument referencing an incremental change description.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:31:59 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.incremental_dataset_arg_description = None  # Placeholder for IncrementalDatasetArgDescription
        self.incremental_dataset = ChangeSet()  # Associated incremental dataset (ChangeSet)
        # Assuming ModelOperationArg and ChangeSet are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
