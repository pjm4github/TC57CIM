# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from IEC61970.Base.Core.RegularIntervalSchedule import RegularIntervalSchedule


class ResourcePerformanceTimeSeriesFactor(RegularIntervalSchedule):
    """
    Represents the performance of a resource as time series data for a specified
    time period, time interval, and evaluation criteria.
    @author mwald
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        """
        Type of the time series data, e.g. baseline data, meter read data, computed
        performance data.
        """
        self.time_series_data_type = ""

        """
        Optional description of the time series data, e.g. baseline data, meter read
        data, computed performance data.
        """
        self.time_series_description = ""

        """
        Description for the value1 contained within the TimeSeriesFactor.
        """
        self.value1_description = ""

        """
        Description for the value2 contained within the TimeSeriesFactor.
        """
        self.value2_description = ""
