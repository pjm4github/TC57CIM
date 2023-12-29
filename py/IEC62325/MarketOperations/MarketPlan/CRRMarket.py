from IEC62325.MarketOperations.MarketPlan.Market import Market


class CRRMarket(Market):
    """
    Model that describes the Congestion Revenue Rights Auction Market.
    @created 28-Dec-2023 8:11:21 PM
    """

    def __init__(self):
        # labelID - an ID for a set of apnodes/pnodes used in a CRR market
        super().__init__()
        self.labelID = ""