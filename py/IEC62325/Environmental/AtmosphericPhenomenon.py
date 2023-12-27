# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# environmental.py

from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Speed import Speed
from IEC62325.Environmental.EnvDomain.Bearing import Bearing
from IEC62325.Environmental.EnvDomain.RelativeDisplacement import RelativeDisplacement
from IEC62325.Environmental.EnvironmentalPhenomenon import EnvironmentalPhenomenon


class AtmosphericPhenomenon(EnvironmentalPhenomenon):
    #  * An atmospheric phenomenon with a base and altitude providing the vertical
    #  * coverage (combined with the Location to provide three-dimensional space).
    #  * @author mcmorran
    #  * @version 1.0
    #  * @created 25-Dec-2023 9:21:22 PM

    def __init__(self):
        super().__init__()
        self.altitude = RelativeDisplacement()  # The maximum altitude of the phenomenon.
        self.base = RelativeDisplacement()  # The base altitude of the phenomenon.
        self.direction = Bearing()  # The direction the phenomenon is moving.
        self.max_coverage = PerCent()  # The maximum percentage coverage
        self.min_coverage = PerCent()  # The minimum percentage coverage
        self.speed = Speed()  # The speed of the phenomenon
