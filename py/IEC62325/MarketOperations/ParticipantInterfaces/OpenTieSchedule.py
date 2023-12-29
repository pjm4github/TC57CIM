# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.ParticipantInterfaces.BidHourlySchedule import BidHourlySchedule


class OpenTieSchedule(BidHourlySchedule):
    """
    Result of bid validation against conditions that may exist on an interchange
    that becomes disconnected or is heavily discounted with respect the MW flow.
    *
    This schedule is assocated with the hourly parameters in a resource bid.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """
    def __init__(self):
        super().__init__()
        self.value = True

