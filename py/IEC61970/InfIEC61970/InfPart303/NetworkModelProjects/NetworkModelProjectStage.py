# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 17:13:56 2024
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectComponent import \
    NetworkModelProjectComponent
from IEC61970.Part303.GenericDataset.ChangeSet import ChangeSet


class NetworkModelProjectStage(NetworkModelProjectComponent):
    """
    @author SELAOST1
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()
        self.changeset_version = int()  # changesetVersion
        self.commissioned_date = DateTime()  # commissionedDate
        self.planned_commissioned_date = DateTime()  # plannedCommissionedDate
        self.m_change_set = ChangeSet()  # m_ChangeSet
