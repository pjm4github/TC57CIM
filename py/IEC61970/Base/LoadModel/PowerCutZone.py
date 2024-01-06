# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:30:57 2024
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Wires.EnergyConsumer import EnergyConsumer


class PowerCutZone(PowerSystemResource):
    """
    An area or zone of the power system which is used for load shedding purposes.
    @created 03-Jan-2024 10:44:40 PM
    """

    def __init__(self):
        super().__init__()
        # First level (amount) of load to cut as a percentage of total zone load.
        self.cut_level_1 = PerCent()  # TypicalValues.PERCENT as an argument to the PerCent class method call.
        # Second level (amount) of load to cut as a percentage of total zone load.
        self.cut_level_2 = PerCent()  # TypicalValues.PERCENT as an argument to the PerCent class method call.
        # Energy consumer is assigned to the power cut zone.
        self.energy_consumers = EnergyConsumer()  # EnergyConsumer class method call.

