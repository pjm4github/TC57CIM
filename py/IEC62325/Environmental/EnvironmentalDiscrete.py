# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Meas.Discrete import Discrete
from IEC62325.Environmental.EnvDomain.EnvironmentalDiscreteKind import EnvironmentalDiscreteKind
from IEC62325.Environmental.EnvironmentalInformation import EnvironmentalInformation


class EnvironmentalDiscrete(Discrete):
    """
    Discrete (integer) measurement of relevance in the environmental domain.
    @author ppbr003
    @version 1.0
    @created 25-dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        # Kind of environmental discrete (integer).
        self.kind = EnvironmentalDiscreteKind.CLOUD_COVER

        # Observation or forecast with which this environmental discrete (integer) is associated.
        self.environmental_information = EnvironmentalInformation()