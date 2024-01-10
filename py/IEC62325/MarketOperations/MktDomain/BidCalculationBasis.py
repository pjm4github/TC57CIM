# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class BidCalculationBasis(Enum):
    LMP_BASED = 1  # Based on prices paid at particular pricing location
    COST_BASED = 2  # Based on unit generation characteristics and a cost of fuel
    NEGOTIATED = 3  # An amount negotiated with the designated Independent Entity
