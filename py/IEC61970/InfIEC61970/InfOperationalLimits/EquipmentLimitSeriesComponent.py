# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Core.Equipment import Equipment
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class EquipmentLimitSeriesComponent(IdentifiedObject):
    """
    This represents one instance of equipment that contributes to the calculation of an operational limit.
    """
    def __init__(self):
        super().__init__()
        self.equipment = Equipment()  # Equipment contributing toward the series limit.

# end EquipmentLimitSeriesComponent
