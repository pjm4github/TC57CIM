# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional


class PnodeDistributionFactor:
    """
    This class allows SC to input different distribution factors for pricing node.
    @created 28-Dec-2023 12:19:30 PM
    """

    def __init__(self) -> None:
        """
        Constructor for PnodeDistributionFactor
        """
        self.factor: float = 0.0  # Used to calculate "participation" of Pnode in an AggregatePnode.
        self.off_peak: Optional[str] = ''  # Indication that this distribution factor is to apply during off-peak.
        self.on_peak: Optional[str] = ''  # Indication that this factor is to apply during Peak periods.
        self.pod_loss_factor: float = 0.0  # Point of delivery loss factor
