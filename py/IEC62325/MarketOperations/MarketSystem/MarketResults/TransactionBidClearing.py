# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors


class TransactionBidClearing(MarketFactors):
    """
    * Contains the intervals relavent for the associated TransactionBidResults. For
    * example, Day Ahead cleared results for the transaction bids for each interval
    * of the market day.
    * @created 28-Dec-2023 8:26:36 PM
    """
    def __init__(self) -> None:
        super().__init__()
