# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from IEC61970.Base.Meas.StringMeasurement import StringMeasurement
from IEC62325.Environmental.ClassificationCondition import ClassificationCondition
from IEC62325.Environmental.EnvironmentalInformation import EnvironmentalInformation


class EnvironmentalStringMeasurement(StringMeasurement):
    """
    String measurement of relevance in the environmental domain.
    @author ppbr003
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        # Classification condition which this string measurement helps define.
        self.classification_condition = ClassificationCondition()

        # Observation or forecast with which this environmental string is associated.
        self.environmental_information = EnvironmentalInformation()
