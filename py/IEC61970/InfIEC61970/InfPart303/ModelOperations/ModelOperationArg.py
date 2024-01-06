from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ModelOperationArg(IdentifiedObject):
    """
    Describes the role a dataset plays in a model operation. The role is
    applicable only in the context of a single operation.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.sequence_number = int()  # The sequence number of the argument in an operation
        self.model_operation = None  # Placeholder for the associated ModelOperation
        # Assuming ModelOperation is a previously defined class
        # If ModelOperation is not defined, this will raise an error and needs to be implemented
