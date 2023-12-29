# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class MarketType(Enum):
    DAM = 1  # Day ahead market
    RTM = 2  # Real time market
    HAM = 3  # Hour Ahead Market
    RUC = 4  # Residual Unit Commitment
