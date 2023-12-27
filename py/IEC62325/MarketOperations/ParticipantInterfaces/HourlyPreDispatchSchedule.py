# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.ParticipantInterfaces.BidHourlySchedule import BidHourlySchedule


class HourlyPreDispatchSchedule(BidHourlySchedule):
    """
    An indicator specifying that a resource shall have an Hourly Pre-Dispatch. The
    resource could be a RegisteredGenerator or a RegisteredInterTie.

    This schedule is assocated with the hourly parameters in a resource bid.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        """
        Flag defining that for this hour in the resource bid the resource shall have an
        hourly pre-dispatch.
        """
        self.value = False

