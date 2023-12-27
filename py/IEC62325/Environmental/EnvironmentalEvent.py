# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.ActivityRecord import ActivityRecord
from IEC62325.Environmental.EnvironmentalInformation import EnvironmentalInformation


class EnvironmentalEvent(ActivityRecord):
    """
    An environmental event to which one or more forecasts or observations may be
    tied and which may relate to or affect one or more assets.
    This class is intended to be used as a means of grouping forecasts and/or
    observations and could be used for a variety of purposes, including:
        - to define a 'named' event like Hurricane Katrina and allow the historic
        (or forecast) values for phenomena and measurements (precipitation,
        temperature) across time to be associated with it
        - to identify assets that were (or are forecast to be) affected by a
        phenomenon or set of measurements
    """

    def __init__(self):
        """
        Forecast or observation related to this environmental event.
        """
        super().__init__()
        self.environmental_information = EnvironmentalInformation()
