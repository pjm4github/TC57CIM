# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from enum import Enum

class CustomerBillingKind(Enum):
    """
    Kind of customer billing.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 9:26:37 PM
    """
    CONSOLIDATED_ESS = 0  # Consolidated bill from energy service supplier (ESS).
    CONSOLIDATED_UDC = 1  # Consolidated bill from utility distribution company (UDC).
    SEPARATE_ESS_UDC = 2   # Separate bills from ESS and UDC.
    OTHER = 3
