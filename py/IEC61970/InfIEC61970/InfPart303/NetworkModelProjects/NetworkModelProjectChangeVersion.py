from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectChange import NetworkModelProjectChange
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectState import NetworkModelProjectState
from IEC61970.Part303.GenericDataset.ChangeSet import ChangeSet


class NetworkModelProjectChangeVersion(IdentifiedObject):
    """
    Describes the status and the planned implementation of the associated change
    set into the as-built model. Instances of this class are considered immutable.
    Author: sveinols
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.comment = str()  # Comment describing changes in this version
        self.effective_date_time = DateTime()  # Date/time the change set is included in the model
        self.time_stamp = DateTime()  # Date/time this version was finalized
        self.change_set = ChangeSet()  # Details of model changes for this project
        self.network_model_project_change = NetworkModelProjectChange()  # Persistent network model project change
        self.superceded_by = None  # Project version that will supercede this one
        self.network_model_project_state = NetworkModelProjectState()  # State of this network model project version
