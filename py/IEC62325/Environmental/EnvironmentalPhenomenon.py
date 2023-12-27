# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC62325.Environmental.EnvironmentalInformation import EnvironmentalInformation
from IEC62325.Environmental.EnvironmentalLocationType import EnvironmentalLocationType
from IEC62325.Environmental.PhenomenonClassification import PhenomenonClassification


class EnvironmentalPhenomenon:
    """
    The actual or forecast characteristics of an environmental phenomenon at a
    specific point in time (or during a specific time interval) that may have both
    a center and area/line location.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        # The timestamp of the phenomenon as a single point or time interval.
        self.time_interval = DateTimeInterval()

        # The forecast or observation of which this phenomenon description is a part.
        self.environmental_information = EnvironmentalInformation()

        # Location of relevance to this environmental phenomenon.
        self.environmental_location_kind = EnvironmentalLocationType()

        # The classification of this phenomenon.
        self.phenomenon_classification = PhenomenonClassification()
