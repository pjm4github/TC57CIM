from IEC61970.Part303.GenericDataset.DataSetMember import DataSetMember
from IEC61970.Part303.GenericDataset.InstanceSet import InstanceSet


class InstanceSetMember(DataSetMember):
    """
    A description of a version of instance data.
    Author: SELAOST1
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.instance_set = InstanceSet()  # Dataset containing the data objects
