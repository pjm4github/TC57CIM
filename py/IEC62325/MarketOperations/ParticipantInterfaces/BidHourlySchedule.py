# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.RegularIntervalSchedule import RegularIntervalSchedule
from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid

"""
Containment for bid hourly parameters that are not product dependent.
@author mspivbe2
@version 1.0
@created 25-Dec-2023 9:21:22 PM
"""


class BidHourlySchedule(RegularIntervalSchedule):

    def __init__(self):
        super().__init__()
        self.bid = Bid()
