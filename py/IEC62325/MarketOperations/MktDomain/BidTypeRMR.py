# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class BidTypeRMR(Enum):
    """
    Bid self schedule type has two types as the required output of requirements and
    qualified pre-dispatch.
    """
    REQUIREMENTS = 1  # Qualified pre-dispatch bid self schedule type.
    QUALIFIED_PREDISPATCH = 2  # Output of requirements bid self schedule type.
