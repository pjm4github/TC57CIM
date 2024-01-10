# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource


class AirCompressor(PowerSystemResource):
    """
    Combustion turbine air compressor which is an integral part of a compressed air
    energy storage (CAES) plant.
    @created 02-Jan-2024 10:50:50 PM
    """

    def __init__(self):
        super().__init__()
        # Rating of the CAES air compressor.
        self.air_compressor_rating = 0.0  # Typical value
