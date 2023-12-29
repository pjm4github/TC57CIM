# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Length import Length
from IEC62325.Environmental.AtmosphericPhenomenon import AtmosphericPhenomenon
from IEC62325.Environmental.EnvDomain.ParticulateDensity import ParticulateDensity

"""
* An ash cloud formed as a result of a volcanic eruption.
* @author mcmorran
* @version 1.0
* @created 25-Dec-2023 9:21:23 PM
"""
class VolcanicAshCloud(AtmosphericPhenomenon):

    """
    Particulate density of the ash cloud during the time interval.
    """
    def __init__(self):
        super().__init__()
        self.density = ParticulateDensity()
        self.particle_size = Length()

    """
    The diameter of the particles during the time interval.
    """
    def set_particle_size(self, particle_size):
        self.particle_size = Length(particle_size)
