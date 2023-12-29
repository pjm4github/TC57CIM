# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum


class TradeStatusType(Enum):
    RJ = 1  # Rejected Trade
    I = 2   # Invalid Trade
    V = 3   # Valid Trade
    M = 4   # Modified Trade
    CV = 5  # Conditionally Valid Trade
    CM = 6  # Conditionally Modified Trade
    CI = 7  # Conditionally Invalid Trade
    CX = 8  # Cancelled Trade
    O = 9   # Obsolete Trade
    MT = 10  # Matched Trade
    U = 11  # Unmatched Trade
