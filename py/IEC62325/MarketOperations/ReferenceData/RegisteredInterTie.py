# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MktDomain.EnergyProductType import EnergyProductType
from IEC62325.MarketOperations.MktDomain.InterTieDirection import InterTieDirection
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo
from IEC62325.MarketOperations.ParticipantInterfaces.InterTieDispatchResponse import InterTieDispatchResponse

class RegisteredInterTie(RegisteredResource):
    """
    This class represents the inter tie resource.
    @created 28-Dec-2023 12:21:16 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.direction: Optional[InterTieDirection] = InterTieDirection.EXPORT

        # Indicates the direction (export/import) of an InterTie resource.
        self.energy_product_type: Optional[EnergyProductType] = EnergyProductType.DYN

        # Under each major product type, the commodity type can be applied to further specify the type.
        self.is_dc_tie: Optional[YesNo] = YesNo.NO

        # Flag to indicate whether this Inter-tie is a DC Tie.
        self.is_dynamic_interchange: Optional[YesNo] = YesNo.NO

        # Specifies whether the inter-tie resource is registered for the dynamic interchange.
        self.min_hourly_block_limit: Optional[int] = 0
        # The registered upper bound of minimum hourly block for an Inter-Tie Resource.
        self.inter_tie_dispatch_response: Optional[InterTieDispatchResponse] = InterTieDispatchResponse()
