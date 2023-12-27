# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PerCent import PerCent


class Charge(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.fixed_portion = None
        self.kind = None
        self.variable_portion = PerCent()
        self.child_charges = None
