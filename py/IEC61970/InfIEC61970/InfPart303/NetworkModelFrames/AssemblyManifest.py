# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:55:15 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames import CompleteModel_TO_BE_DELETED
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.ModelPartVersion import ModelPartVersion


class AssemblyManifest(IdentifiedObject):
    """
    A collection of model parts when combined form a case or part of a case.
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:31:54 PM
    """

    def __init__(self):
        super().__init__()
        self.m_model_part_version = ModelPartVersion()  # Assume ModelPartVersion is a class method
        self.m_complete_model_to_be_deleted = CompleteModel_TO_BE_DELETED  # Assume CompleteModel.TO_BE_DELETED is a typical value and a class name
