# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.Environmental.EnvDomain.RelativeDisplacement import RelativeDisplacement
from IEC62325.Environmental.GeosphericPhenomenon import GeosphericPhenomenon


class Earthquake(GeosphericPhenomenon):

    def __init__(self):
        # 	 * The depth below the earth's surface of the earthquake's focal point.
        super().__init__()
        self.focal_depth = RelativeDisplacement()

        # The intensity of the earthquake as defined by the Modified Mercalli Intensity
        # (MMI) scale. Possible values are 1-12, corresponding to I-XII.
        self.intensity = 0

        # The magnitude of the earthquake as defined on the Moment Magnitude
        # (M<sub>w</sub>) scale, which measures the size of earthquakes in terms of the
        # energy released. Must be greater than zero.
        self.magnitude = 0.0
