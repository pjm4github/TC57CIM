# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ParticipantInterfaces.GeneratingBid import GeneratingBid


class BidSet(IdentifiedObject):
    """
    * As set of mutually exclusive bids for which a maximum of one may be scheduled.
    * Of these generating bids, only one generating bid can be scheduled at a time.
    * @created 28-Dec-2023 5:20:00 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.generating_bids = [GeneratingBid()]
