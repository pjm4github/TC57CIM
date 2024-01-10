# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Meas.MeasurementValueQuality import MeasurementValueQuality


class DiscreteMeasurementValueQuality(MeasurementValueQuality):
    """Measurement quality flags for Discrete Values.

    @created 27-Dec-2023 3:27:25 PM
    """
    def __init__(self) -> None:
        """Initialize DiscreteMeasurementValueQuality."""
        super().__init__()
        """Switch Manual Replace Indicator. Flag indicating that the switch is manual
        replace."""
        self.manual_replace_indicator: bool = False
        """Removed From Operation Indicator. Flag indicating that the switch is removed
        from operation."""
        self.remove_from_operation_indicator: bool = False


