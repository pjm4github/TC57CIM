# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
"""
Defines the state of a transaction.
@author mspivbe2
@version 1.0
@created 25-Dec-2023 9:21:22 PM
"""
from enum import StrEnum


class EnergyTransactionType(StrEnum):
    """
    Enum for energy transaction type
    """
    APPROVE = "approve"
    DENY = "deny"
    STUDY = "study"
