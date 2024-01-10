from IEC61970.Base.Generation.GenerationTrainingSimulation.CombustionTurbine import CombustionTurbine
from IEC61970.Base.Generation.GenerationTrainingSimulation.FossilSteamSupply import FossilSteamSupply


class HeatRecoveryBoiler(FossilSteamSupply):
    """
    The heat recovery system associated with combustion turbines in order to
    produce steam for combined cycle plants.
    Created: 02-Jan-2024 11:05:44 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.steam_supply_rating2 = 0.0  # Steam supply rating in kilopounds per hour, if dual pressure boiler
        self.combustion_turbines = CombustionTurbine()  # Associated combustion turbine
        # Assuming FossilSteamSupply, Float, and CombustionTurbine are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
