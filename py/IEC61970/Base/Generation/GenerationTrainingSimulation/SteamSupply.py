from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Generation.GenerationTrainingSimulation.SteamTurbine import SteamTurbine


class SteamSupply(PowerSystemResource):
    """
    Steam supply for steam turbine.
    Created: 02-Jan-2024 11:06:31 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.steam_supply_rating = 0.0  # Rating of steam supply
        self.steam_turbines = SteamTurbine()  # Steam turbines may have steam supplied by this steam supply
        # Assuming PowerSystemResource, Float, and SteamTurbine are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
