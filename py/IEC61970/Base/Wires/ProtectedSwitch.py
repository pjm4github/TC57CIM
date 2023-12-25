# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Switch import Switch


class RecloseSequence:
    pass


class ProtectedSwitch(Switch):

    def __init__(self) -> None:
        super().__init__()
        self.breaking_capacity = CurrentFlow()
        self.reclose_sequences = RecloseSequence()

    def get_breaking_capacity(self) -> CurrentFlow:
        return self.breaking_capacity

    def get_reclose_sequences(self) -> RecloseSequence:
        return self.reclose_sequences

    def set_breaking_capacity(self, new_val: CurrentFlow) -> None:
        self.breaking_capacity = new_val

    def set_reclose_sequences(self, new_val: RecloseSequence) -> None:
        self.reclose_sequences = new_val
