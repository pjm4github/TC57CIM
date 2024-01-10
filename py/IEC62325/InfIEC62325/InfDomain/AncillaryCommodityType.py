# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum


class AncillaryCommodityType(Enum):
    REGUP = 1  # regulation up
    REGDN = 2  # regulation down
    SPIN = 3   # spinning reserve
    NONSPIN = 4  # non-spinning reserve
