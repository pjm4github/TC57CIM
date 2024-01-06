from IEC62325.MarketOperations.ReferenceData.AggregatedPnode import AggregatedPnode


class TradingHubValues:
    """
    Models prices at Trading Hubs.
    """
    def __init__(self):
        self.price = 1.0  # Price at the trading hub, varies by market type (DA hourly, RTM 5-minute)
        self.aggregated_pnode = AggregatedPnode()  # Associated AggregatedPnode
