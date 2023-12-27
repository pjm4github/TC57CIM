# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Operations.SwitchActionKind import SwitchActionKind
from IEC61968.Operations.SwitchingAction import SwitchingAction
from IEC61970.Base.Wires.Cut import Cut


class CutAction(SwitchingAction):
    
    def __init__(self):
        super().__init__()
        self.kind = SwitchActionKind.OPEN  # Switching action to perform
        self.cut = Cut()  # Cut on which this action is taken

