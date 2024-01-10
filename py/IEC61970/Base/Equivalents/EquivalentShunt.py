from IEC61970.Base.Domain.Conductance import Conductance
from IEC61970.Base.Domain.Susceptance import Susceptance
from IEC61970.Base.Equivalents.EquivalentEquipment import EquivalentEquipment


class EquivalentShunt(EquivalentEquipment):
    """
    The class represents equivalent shunts.
    Created: 07-Jan-2024 10:00:43 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.b = Susceptance()  # Positive sequence shunt susceptance
        self.g = Conductance()  # Positive sequence shunt conductance
