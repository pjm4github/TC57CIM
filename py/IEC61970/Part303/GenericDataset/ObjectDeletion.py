from IEC61970.Part303.GenericDataset.ChangeSetMember import ChangeSetMember


class ObjectDeletion(ChangeSetMember):
    """
    An object is to be deleted in the context.
    Author: 222206
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        # No additional attributes are defined in the provided Java class
