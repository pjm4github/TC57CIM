# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Operations.SwitchingAction import SwitchingAction
from IEC61970.Base.Meas.Control import Control


class ControlAction(SwitchingAction):
    
    def __init__(self):
        super().__init__()
        self.analog_value = 0.0
        self.discrete_value = 0
        self.control = Control()
