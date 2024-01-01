# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MarketSystem.MarketResults.MPMTestResults import MPMTestResults
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class MpmClearing(MarketFactors):
    def __init__(self) -> None:
        super().__init__()
        self.lmpm_final_flagOptional[YesNo] = YesNo.NO
        self.mitigation_occurred_flagOptional[YesNo] = YesNo.NO
        self.smpm_final_flagOptional[YesNo] = YesNo.NO
        self.mpm_test_resultsOptional[MPMTestResults] = MPMTestResults()
