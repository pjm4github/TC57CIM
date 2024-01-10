from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketQualitySystem.TradingHubValues import TradingHubValues
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType


class TradingHubPrice:
    """
    Models prices at Trading Hubs, interval based.
    """
    def __init__(self):
        self.interval_start_time = DateTime()  # Start time of the interval
        self.market_type = MarketType.RUC  # Type of market
        self.update_time_stamp = DateTime()  # Timestamp of the last update
        self.update_user = str()  # User who last updated the record
        self.trading_hub_values = TradingHubValues()  # Associated TradingHubValues
