# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023

from IEC62325.MarketOperations.MarketSystem.MarketResults.MitigatedBidClearing import MitigatedBidClearing
from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid


class RmrDetermination:
    """Indicates whether unit is a reliability must run unit: required to be on to
    satisfy Grid Code Reliability criteria, load demand, or voltage support.
    @created 28-Dec-2023 8:24:53 PM
    """

    def __init__(self) -> None:
        self.bid = Bid()
        self.mitigated_bid_clearing = MitigatedBidClearing()