# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Core.RegularIntervalSchedule import RegularIntervalSchedule
from IEC62325.MarketOperations.MktDomain.LoadForecastType import LoadForecastType
from IEC62325.MarketOperations.ReferenceData.AggregateNode import AggregateNode


class AreaLoadCurve(RegularIntervalSchedule):
    """
    Area load curve definition.
    @created 27-Dec-2023 3:24:51 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.forecast_type: LoadForecastType = LoadForecastType.LFZ
        self.aggregate_node: AggregateNode = AggregateNode()
