# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:55:15 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.ModelPartSpecification import ModelPartSpecification


class AssemblyDescription(IdentifiedObject):
    """
    A description for how to assemble model parts for a specific purpose.
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:31:54 PM
    """

    def __init__(self):
        super().__init__()
        # The models that are part of the assembly description.
        self.model_specification = ModelPartSpecification()  # assuming typical_value is provided
