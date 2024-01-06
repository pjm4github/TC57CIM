# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:55:15 2024
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.CompleteModel_TO_BE_DELETED import CompleteModelToBeDeleted
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.ModelPartSpecification import ModelPartSpecification
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.Model_TO_BE_DELETED import ModelToBeDeleted
from IEC61970.Part303.GenericDataset.DataSet import DataSet


class ModelPartVersion(ModelToBeDeleted):
    """
    This is a version of a part of a model.
    New instances of this class with new identity are instantiated upon changes to the content of this class or changes
    to the associated data set. Instances of this class are considered immutable.
    The case audit trail can reference this immutable data to exactly reproduce a case.
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """

    def __init__(self):
        super().__init__()
        self.model_specification = ModelPartSpecification()  # Model specification of the model
        self.m_data_set = DataSet()  # The associated data set
        self.m_complete_model_to_be_deleted = CompleteModelToBeDeleted()  # Complete model to be deleted
