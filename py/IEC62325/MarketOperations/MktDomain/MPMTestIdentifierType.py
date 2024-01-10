# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class MpmTestIdentifierType(Enum):
    """
    Market power mitigation test identifier type, for example:
    *
    1 ? Global Price Test
    2 ? Global Conduct Test
    3 ? Global Impact Test
    4 ? Local Price Test
    5 ? Local Conduct Test
    6 ? Local Impact Test
    """
    GLOBAL_PRICE_TEST = 1  # * 1 - Global Price Test.
    GLOBAL_CONDUCT_TEST = 2  # * 2 - Global Conduct Test.
    GLOBAL_IMPACT_TEST = 3  # * 3 - Global Impact Test.
    LOCAL_PRICE_TEST = 4
    LOCAL_CONDUCT_TEST = 5
    LOCAL_IMPACT_TEST = 6
