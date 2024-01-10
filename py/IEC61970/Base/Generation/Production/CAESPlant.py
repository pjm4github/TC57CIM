# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.RealEnergy import RealEnergy
from IEC61970.Base.Generation.Production.AirCompressor import AirCompressor
from IEC61970.Base.Generation.Production.ThermalGeneratingUnit import ThermalGeneratingUnit


class CAESPlant(PowerSystemResource):
    """
    Compressed air energy storage plant.
    @created 02-Jan-2024 10:51:26 PM
    """

    def __init__(self):
        super().__init__()
        # The rated energy storage capacity.
        self.energy_storage_capacity = RealEnergy()  # Typical value
        # The CAES plant's gross rated generating capacity.
        self.rated_capacity_p = ActivePower()  # Typical value
        # A thermal generating unit may be a member of a compressed air energy storage plant
        self.thermal_generating_unit = ThermalGeneratingUnit()  # Typical value
        # An air compressor may be a member of a compressed air energy storage plant.
        self.air_compressor = AirCompressor()  # Typical value
