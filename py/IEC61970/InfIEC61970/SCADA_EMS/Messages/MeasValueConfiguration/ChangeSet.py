# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:08:40 2024
from IEC61970.Part303.GenericDataset.ChangeSetMember import ChangeSetMember
from IEC61970.Part303.GenericDataset.DataSet import DataSet


class ChangeSet(DataSet):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:31:54 PM
    A class representing a Change Set
    """

    def __init__(self):
        super().__init__()
        self.m_change_set_member = ChangeSetMember()
