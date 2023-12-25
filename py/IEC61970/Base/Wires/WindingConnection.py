# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum


class WindingConnection(Enum):

    D = 1  # Delta
    Y = 2  # Wye
    Z = 3  # ZigZag
    YN = 4  # Wye, with neutral brought out for grounding.
    ZN = 5  # ZigZag, with neutral brought out for grounding.
    A = 6  # Autotransformer common winding
    I = 7  # Independent winding, for single-phase connections
