from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Money import Money
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors

class SecurityConstraintsClearing(MarketFactors):
    """
    Binding security constrained clearing results posted for a given settlement period.
    """
    def __init__(self):
        super().__init__()
        self.mw_flow = ActivePower()  # 	 * Optimal MW flow
        self.mw_limit = ActivePower()  # 	 * Binding MW limit.
        self.shadow_price = Money() # 	 * Security constraint shadow price.
