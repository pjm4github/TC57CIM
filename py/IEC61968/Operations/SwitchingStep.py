# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.SwitchingAction import SwitchingAction
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.SwitchingStepGroup import SwitchingStepGroup


class SwitchingStep:
    def __init__(self):
        self.sequence_number = 0
        self.switching_step_group = SwitchingStepGroup()
        self.switching_action = SwitchingAction()
