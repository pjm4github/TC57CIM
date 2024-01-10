from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.AlternateModels.AlternateModelGroup import AlternateModelGroup
from IEC61970.Part303.GenericDataset.DataSet import DataSet


class AlternateModel(IdentifiedObject):
    """
    Represents an alternate model for a group of alternate models, where one alternate is used.
    """

    def __init__(self):
        super().__init__()
        self.alternate_model_group = AlternateModelGroup()  # The group of alternate models for which one alternate
        # is used.
        self.dataset = DataSet()  # The data belonging to the alternate model.

# end AlternateModel
