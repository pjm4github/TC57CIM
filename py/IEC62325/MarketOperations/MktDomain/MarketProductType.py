# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class MarketProductType(Enum):
    """
    For example:
    Energy, Reg Up, Reg Down, Spin Reserve, Nonspin Reserve, RUC, Load Following Up,
    and Load Following Down.
    """
    EN = 1  # energy type
    RU = 2  # regulation up
    RD = 3  # regulation down
    SR = 4  # spinning reserve
    NR = 5  # non spinning reserve
    RC = 6  # Residual Unit Commitment
    LFU = 7  # Load following up
    LFD = 8  # Load following down
    REG = 9  # Regulation
