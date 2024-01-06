# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:20:57 2024
from IEC61970.Base.Wires.EnergyConsumer import EnergyConsumer


class ConformLoad(EnergyConsumer):
    """
    * ConformLoad represent loads that follow a daily load change pattern where the
    * pattern can be used to scale the load with a system load.
    * @created 03-Jan-2024 10:44:40 PM
    """
    def __init__(self) -> None:
        super().__init__()
