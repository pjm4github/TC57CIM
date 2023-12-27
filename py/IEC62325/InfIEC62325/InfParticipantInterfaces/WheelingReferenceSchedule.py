# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC62325.MarketOperations.ParticipantInterfaces.BidHourlySchedule import BidHourlySchedule


# A unique identifier of a wheeling transaction. A wheeling transaction is a
# balanced Energy exchange among Supply and Demand Resources.
# This schedule is assocated with the hourly parameters in a resource bid.
# @author mspivbe2
# @version 1.0
# @created 25-Dec-2023 9:21:23 PM

class WheelingReferenceSchedule(BidHourlySchedule):

    def __init__(self):
        super().__init__()
        self.value = ""
