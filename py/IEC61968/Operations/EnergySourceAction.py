# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Operations.SwitchingAction import SwitchingAction
from IEC61970.Base.Wires.EnergySource import EnergySource


class EnergySourceAction(SwitchingAction):

    def __init__(self):
        super().__init__()
        self.kind = None
        self.energy_source = EnergySource()
