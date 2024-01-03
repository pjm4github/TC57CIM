# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Reactance import Reactance
from IEC61970.Base.Wires.TransformerEnd import TransformerEnd

class WindingInsulation(IdentifiedObject):
    """Winding insulation condition as a result of a test."""
    def __init__(self):
        super().__init__()
        self.insulation_pf_status = ""  # Status of Winding Insulation Power Factor
        self.insulation_resistance = ""  # Status of Winding Insulation Resistance
        self.leakage_reactance = Reactance()  # Leakage reactance measured at the "from" winding
        self.status = Status()
        self.to_winding = TransformerEnd()
        self.from_winding = TransformerEnd()
