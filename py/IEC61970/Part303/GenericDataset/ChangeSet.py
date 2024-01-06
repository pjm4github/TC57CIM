from IEC61970.Part303.GenericDataset.DataSet import DataSet


class ChangeSet(DataSet):
    """
    Describes a set of changes that can be applied in different situations. A
    given registered target object MRID may only be referenced once by the
    contained change set members.
    Author: 222206
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        # Assuming DataSet is a previously defined class
        # If DataSet is not defined, this will raise an error and needs to be implemented
