# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketSystem.MarketResults.TransactionBidClearing import TransactionBidClearing
from IEC62325.MarketOperations.ParticipantInterfaces.TransactionBid import TransactionBid


class TransactionBidResults(IdentifiedObject):
    """
    Contains the cleared results for each TransactionBid submitted to and accepted
    by the market.
    @created 28-Dec-2023 8:26:45 PM
    """
    
    def __init__(self) -> None:
        """
        Default constructor
        """
        super().__init__()
        self.cleared_mw: float = 0.0  # The market transaction megawatt
        self.cleared_price: float = 0.0  # The price of the market transaction
        self.transaction_bidOptional[TransactionBid] = TransactionBid()
        self.transaction_bid_clearingOptional[TransactionBidClearing] = TransactionBidClearing()
