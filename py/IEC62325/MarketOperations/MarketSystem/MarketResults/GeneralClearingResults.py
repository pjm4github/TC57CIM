# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

class GeneralClearingResults:
    """
    Provides the adjusted load forecast value on a load forecast zone basis.
    @created 28-Dec-2023 8:21:31 PM
    """

    def __init__(self) -> None:
        """
        Load Prediction/Forecast (MW), by Time Period (5', 10', 15')
        """
        self.load_forecast: float = 0.0

        """
        Amount of load in the control zone
        Attribute Usage: hourly load value for the specific area
        """
        self.total_load: float = 0.0

        """
        Amount of interchange for the control zone
        Attribute Usage: hourly interchange value for the specific area
        """
        self.total_net_interchange: float = 0.0
