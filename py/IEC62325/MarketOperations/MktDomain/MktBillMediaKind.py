# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
"""
Kind of bill media.
@author T. Kostic
@version 1.0
@created 25-dec-2023 9:21:22 PM
"""
from enum import StrEnum


class MktBillMediaKind(StrEnum):
    PAPER = "paper"
    ELECTRONIC = "electronic"
    OTHER = "other"
