# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class MarketProductTypeAsReq(Enum):
    RU = 1  # regulation up
    RD = 2  # regulation down
    SR = 3  # spinning reserve
    NR = 4  # non spinning reserve
    AS = 5  # upward ancillary service
