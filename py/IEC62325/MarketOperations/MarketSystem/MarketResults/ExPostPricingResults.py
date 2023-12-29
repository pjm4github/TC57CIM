# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC62325.MarketOperations.MarketSystem.MarketResults.ExPostPricing import ExPostPricing


class ExPostPricingResults:
    """
    Model of ex-post pricing of nodes.  Includes LMP information, pnode based.
    @created 28-Dec-2023 8:20:55 PM
    """

    def __init__(self) -> None:
        self.congest_lmp: float = 0.0
        """
        Congestion component of Location Marginal Price (LMP) in monetary units per MW;
        congestion component of the hourly LMP at a specific pricing node
        Attribute Usage: Result of the Security, Pricing, and
        Dispatch(SPD)/Simultaneous Feasibility Test(SFT) software and denotes the
        hourly congestion component of LMP for each pricing node.
        """

        self.lmp: float = 0.0
        """
        5 min weighted average LMP; the Location Marginal Price of the Pnode for which
        price calculation is carried out.
        Attribute Usage: 5 min weighted average LMP  to be displayed on UI
        """

        self.loss_lmp: float = 0.0
        """
        Loss component of Location Marginal Price (LMP) in monetary units per MW; loss
        component of the hourly LMP at a specific pricing node
        Attribute Usage: Result of the Security, Pricing, and
        Dispatch(SPD)/Simultaneous Feasibility Test(SFT) software and denotes the
        hourly loss component of LMP for each pricing node.
        """

        self.ex_post_pricing: ExPostPricing = ExPostPricing()
