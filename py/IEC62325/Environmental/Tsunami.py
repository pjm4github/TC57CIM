# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC62325.Environmental.HydrosphericPhenomenon import HydrosphericPhenomenon


class Tsunami(HydrosphericPhenomenon):
    """
    A tsunami (tidal wave), a long high sea wave caused by an earthquake, submarine
    landslide, or other disturbance.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """


    def __init__(self):
        super().__init__()
        # Tsunami intensity on the Papadopoulos-Imamura tsunami intensity scale. Possible
        # values are 1-12, corresponding to I-XII.

        self.intensity = 0

        # Tsunami magnitude in the Tsunami Magnitude Scale (Mt).  Is greater than zero.
        self.magnitude = 0.0
