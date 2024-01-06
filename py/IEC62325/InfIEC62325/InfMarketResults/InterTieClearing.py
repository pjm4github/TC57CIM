from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors


class InterTieClearing(MarketFactors):
    """
    Model of market clearing related to results at the inter-ties. Identifies interval
    @created 28-Dec-2023 8:00:59 PM
    """
    def __init__(self):
        super().__init__()
        self.inter_tie_results = None  # InterTieResults
