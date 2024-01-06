# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:55:15 2024
from IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.ModelAuthoritySet import ModelAuthoritySet


class FrameworkPart(ModelAuthoritySet):
    """
    The type of alternate model frame. For example, it could be generator group
    used to represent generators in state estimator, planning, planning dynamics,
    short circuit, or real-time dynamics etc., but does not specifically represent
    any one alternative model. This need to know what objects to be removed in the
    realization of any one alternate model.
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:31:58 PM
    """

    def __init__(self):
        super().__init__()
        # Model frame type of the model frame.
        self.model_frame_type = ModelFrameType()
