# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.ParticipantInterfaces.BidHourlyProductSchedule import BidHourlyProductSchedule


class PumpingCostSchedule(BidHourlyProductSchedule):
    """
    The operating cost of a Pump Storage Hydro Unit operating as a hydro pump.
    *
    This schedule is assocated with the hourly parameters in a resource bid
    associated with a specific product within the bid.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """
    
    def __init__(self):
        super().__init__()
        self.value = 0.0
