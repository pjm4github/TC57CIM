# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class CommitmentType(Enum):
    """
    For example:
    SELF - Self commitment
    ISO - New commitment for this market period
    UC - Existing commitment that was a hold-over from a previous market
    """
    SELF = 0
    ISO = 1
    UC = 2
