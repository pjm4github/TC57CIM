# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:55:15 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.ModelAuthoritySet import ModelAuthoritySet


class ModelPartSpecification(IdentifiedObject):
    # The type of model.
    # For example, state estimator, planning, planning dynamics, short circuit, or real-time dynamics etc. The model must conform to a profile.
    # @author 222206
    # @version 1.0
    # @created 25-Dec-2023 8:32:00 PM
    
    def __init__(self):
        super().__init__()
        self.framework_part = ModelAuthoritySet()  # Model frame of the model part.
        
