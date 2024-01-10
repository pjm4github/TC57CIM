from IEC61970.Base.Generation.GenerationTrainingSimulation.FossilSteamSupply import FossilSteamSupply


class DrumBoiler(FossilSteamSupply):
    """
    Drum boiler.
    Created: 02-Jan-2024 11:04:53 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.drum_boiler_rating = 0.0  # Rating of drum boiler in steam units
        # Assuming FossilSteamSupply and Float are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
