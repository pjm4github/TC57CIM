# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from IEC62325.MarketOperations.ReferenceData.AggregatedPnode import AggregatedPnode
from IEC62325.MarketOperations.ReferenceData.IndividualPnode import IndividualPnode


class CongestionArea(AggregatedPnode):
    """
    Designated Congestion Area Definition (DCA).
    @created 28-Dec-2023 1:03:25 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.individual_pnode: IndividualPnode = IndividualPnode()
