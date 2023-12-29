# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketSystem.MarketResults.MitigatedBidClearing import MitigatedBidClearing
from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid


class MitigatedBid(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.bid: Bid = Bid()
        self.mitigated_bid_clearing: MitigatedBidClearing = MitigatedBidClearing()
