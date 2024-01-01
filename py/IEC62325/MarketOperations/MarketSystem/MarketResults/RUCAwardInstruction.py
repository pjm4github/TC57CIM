# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from enum import Enum
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime


class MarketProductType(Enum):
    ENERGY = 1
    REGULATION_UP = 2
    REGULATION_DN = 3
    SPINNING_RESERVE = 4
    NON_SPINNING_RESERVE = 5
    OPERATING_RESERVE = 6

class RUCAwardInstruction:
    """
    This class models the information about the RUC awards.
    @created 28-Dec-2023 8:25:11 PM
    """
    
    def __init__(self) -> None:
        """
        Constructor for RUCAwardInstruction.
        """
        self.cleared_price: float = 0.0  # Marginal Price ($/MW) for the commodity
        self.market_product_typeOptional[MarketProductType] = MarketProductType.ENERGY # Major product type
        self.ruc_award: float = 0.0  # The RUC Award of a resource
        self.ruc_capacity: float = 0.0  # The RUC Capacity of a resource
        self.ruc_schedule: float = 0.0  # The RUC Schedule of a resource
        self.update_time_stamp: DateTime = DateTime()
        self.update_type: str = ""
        self.update_user: str = ""
