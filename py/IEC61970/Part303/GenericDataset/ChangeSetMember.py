from IEC61970.Part303.GenericDataset.ChangeSet import ChangeSet
from IEC61970.Part303.GenericDataset.DataSetMember import DataSetMember


class ChangeSetMember(DataSetMember):
    """
    A CRUD-style data object.
    Author: 222206
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.changeset = ChangeSet()  # Placeholder for the dataset containing the data objects (ChangeSet)
        # Assuming ChangeSet is a previously defined class
        # If ChangeSet is not defined, this will raise an error and needs to be implemented
