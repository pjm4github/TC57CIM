# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Optional

from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class ContractDistributionFactor:
    """
    Distribution among resources at the sink point or source point.
    @created 28-Dec-2023 1:03:35 PM
    """

    def __init__(self) -> None:

        # MW value that this resource provides to the overall contract.
        self.factorfloat = 0.0

        # This value will be set to YES if the referenced Cnode is defined as the sink point in the contract.
        self.sink_flag = YesNo.NO

        # This value will be set to YES if the referenced Cnode is defined as the source point in the contract.
        self.source_flag = YesNo.NO
