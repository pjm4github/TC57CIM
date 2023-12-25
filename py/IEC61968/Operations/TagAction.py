# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.OperationalTag import OperationalTag
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.SwitchingAction import SwitchingAction
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.TagActionKind import TagActionKind


class TagAction(SwitchingAction):
    def __init__(self):
        super().__init__()
        self.kind = TagActionKind.VERIFY
        self.operational_tag = OperationalTag()
