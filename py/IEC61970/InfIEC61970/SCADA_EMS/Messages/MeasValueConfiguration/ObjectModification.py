# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:08:40 2024
# public class ObjectModification extends ChangeSetMember {
from IEC61970.Part303.GenericDataset.ChangeSetMember import ChangeSetMember
from IEC61970.Part303.GenericDataset.ObjectReverseModification import ObjectReverseModification


class ObjectModification(ChangeSetMember):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:32:01 PM
    """

    def __init__(self):
        super().__init__()
        self.m_object_reverse_modification = ObjectReverseModification()

