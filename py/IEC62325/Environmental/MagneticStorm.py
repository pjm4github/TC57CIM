# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.Environmental.EnvDomain.MagneticField import MagneticField
from IEC62325.Environmental.SpacePhenomenon import SpacePhenomenon


class MagneticStorm(SpacePhenomenon):

    def __init__(self):
        super().__init__()

        # Change in the disturbance  - storm time (Dst) index. The size of a geomagnetic
        # storm is classified as:
        # - moderate ( -50 nT >minimum of Dst > -100 nT)
        # - intense (-100 nT > minimum Dst > -250 nT) or
        # - super-storm ( minimum of Dst < -250 nT).
        self.change_dst = MagneticField()
