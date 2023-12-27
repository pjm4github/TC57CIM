# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Meas.StringMeasurement import StringMeasurement  # TODO Check for StringMeasurementValue
from IEC62325.Environmental.EnvDomain.CoverageCodeKind import CoverageCodeKind
from IEC62325.Environmental.EnvDomain.IntensityCodeKind import IntensityCodeKind
from IEC62325.Environmental.EnvDomain.WeatherCodeKind import WeatherCodeKind


class EnvironmentalCodedValue(StringMeasurement):
    """
    An environmental value described using a coded value. A triplicate of
    enumerated values representing intensity, coverage, type of weather is used.
    These may be concatenated into the string value.
    @author ppbr003
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        # Code representing the coverage of the weather condition.
        super().__init__()
        self.coverage_kind = CoverageCodeKind.BRIEF

        # Code representing the intensity of the weather condition.
        self.intensity_kind = IntensityCodeKind.HEAVY

        # Probability of weather condition occurring during the time interval expressed
        # as a percentage. Applicable only when weather condition is related to a
        # forecast (not an observation).
        self.probability_percent = PerCent()

        # Code representing the type of weather condition.
        self.weather_kind = WeatherCodeKind.HAIL
