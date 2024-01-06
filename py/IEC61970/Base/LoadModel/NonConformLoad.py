# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:30:57 2024
from IEC61970.Base.Wires.EnergyConsumer import EnergyConsumer


class NonConformLoad(EnergyConsumer):
    """
    NonConformLoad represents loads that do not follow a daily load change pattern
    and changes are not correlated with the daily load change pattern.
    @created 03-Jan-2024 10:44:40 PM
    """

    def __init__(self):
        super().__init__()
        # Add attributes here
        # Typical values used for initialization
        # self.attribute_name = class_name.method_name(typical_value)
