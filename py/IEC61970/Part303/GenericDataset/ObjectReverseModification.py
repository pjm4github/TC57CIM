from IEC61970.Part303.GenericDataset.ChangeSetMember import ChangeSetMember
from IEC61970.Part303.GenericDataset.ObjectModification import ObjectModification


class ObjectReverseModification(ChangeSetMember):
    """
    Used to specify precondition properties for a preconditioned update.
    Author: 222206
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.object_modification = ObjectModification()  # The associated data object representing the update
        # Assuming ObjectModification is a previously defined class
        # If ObjectModification is not defined, this will raise an error and needs to be implemented
