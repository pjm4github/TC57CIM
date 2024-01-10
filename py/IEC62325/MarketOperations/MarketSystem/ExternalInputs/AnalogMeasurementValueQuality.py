# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Meas.MeasurementValueQuality import MeasurementValueQuality


class AnalogMeasurementValueQuality(MeasurementValueQuality):
    """
    Measurement quality flags for Analog Values.
    @created 27-Dec-2023 3:24:40 PM
    """

    def __init__(self) -> None:
        """
        Constructor for AnalogMeasurementValueQuality
        """
        super().__init__()
        self.scada_quality_code: str = ""
