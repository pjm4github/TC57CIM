# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.PerCent import PerCent
from IEC62325.MarketOperations.ReferenceData.SchedulingCoordinator import SchedulingCoordinator


class LoadRatio:
    """
    Representing the ratio of the load share for the associated SC.
    @author USRAKHA
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        Constructor
        """    
        self.interval_end_time = DateTime()
        self.interval_start_time = DateTime()
        #  * Share in percentage of total Market load for the selected time interval.
        self.share = PerCent()
        self.scheduling_coordinator = SchedulingCoordinator()
