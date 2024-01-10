from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Generation.GenerationTrainingSimulation.PrimeMover import PrimeMover


class SteamTurbine(PrimeMover):
    """
    Steam turbine.
    Created: 02-Jan-2024 11:06:43 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.crossover_tc = Seconds()  # Crossover time constant
        self.reheater1_tc = Seconds()  # First reheater time constant
        self.reheater2_tc = Seconds()  # Second reheater time constant
        self.shaft1_power_hp = 0.0  # Fraction of power from shaft 1 high pressure turbine output
        self.shaft1_power_ip = 0.0  # Fraction of power from shaft 1 intermediate pressure turbine output
        self.shaft1_power_lp1 = 0.0  # Fraction of power from shaft 1 first low pressure turbine output
        self.shaft1_power_lp2 = 0.0  # Fraction of power from shaft 1 second low pressure turbine output
        self.shaft2_power_hp = 0.0  # Fraction of power from shaft 2 high pressure turbine output
        self.shaft2_power_ip = 0.0  # Fraction of power from shaft 2 intermediate pressure turbine output
        self.shaft2_power_lp1 = 0.0  # Fraction of power from shaft 2 first low pressure turbine output
        self.shaft2_power_lp2 = 0.0  # Fraction of power from shaft 2 second low pressure turbine output
        self.steam_chest_tc = Seconds()  # Steam chest time constant
        # Assuming PrimeMover, Seconds, and Float are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented

