from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ModelOperation(IdentifiedObject):
    """
    An operation performed on models.
    Author: 222206
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.sequence_number = int()  # Sequence number within an operation sequence, lower is first.
        self.model_operation_description = None  # Placeholder for ModelOperationDescription
        # Assuming ModelOperationDescription is a previously defined class
        # If ModelOperationDescription is not defined, this will raise an error and needs to be implemented
