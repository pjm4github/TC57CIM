# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.ReferenceData.PnodeDistributionFactor import PnodeDistributionFactor


class BidDistributionFactor:
    """
    This class allows SC to input different time intervals for distribution factors.
    
    @created 28-Dec-2023 5:18:43 PM
    """

    def __init__(self) -> None:
        """
        Constructor for BidDistributionFactor
        """
        self.time_interval_end: DateTime = DateTime()
        # End of the time interval n which bid is valid (yyyy-mm-dd hh24: mi: ss)
        
        self.time_interval_start: DateTime = DateTime()
        # Start of the time interval in which bid is valid (yyyy-mm-dd hh24: mi: ss)
        
        self.pnode_distribution_factor: PnodeDistributionFactor = PnodeDistributionFactor()
