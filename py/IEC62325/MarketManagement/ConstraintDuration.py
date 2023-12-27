# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Duration import Duration
from IEC62325.MarketManagement.TimeSeries import TimeSeries


class ConstraintDuration:
    """
    Duration constraint to activate, to put in operation, to deactivate, a given event.
    @author ENTSOE
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        The duration of the constraint.
        """
        self.duration = Duration()
        
        """
        The type of the constraint.
        """
        self.type = ""
        
        self.time_series = TimeSeries()
