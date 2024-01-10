# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:08:40 2024
from IEC61970.Part303.GenericDataset.ChangeSet import ChangeSet
from IEC61970.Part303.GenericDataset.DataSetMember import DataSetMember


class ChangeSetMember(DataSetMember):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:31:55 PM
    """
    def __init__(self):
        super().__init__()
        self.m_change_set = ChangeSet()  # Initializing m_change_set attribute to an instance of ChangeSet class
