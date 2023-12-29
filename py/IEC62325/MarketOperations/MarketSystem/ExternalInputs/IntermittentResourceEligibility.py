# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors


class IntermittentResourceEligibility(MarketFactors):
    """
    Indicates whether unit is eligible for treatment as a intermittent variable
    renewable resource.

    @created 27-Dec-2023 3:29:34 PM
    """

    def __init__(self):
        super().__init__()
        # 	 * Indicates whether a resource is eligible for PIRP program for a given hour
        self.eligibility_status: str = ""
