# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from enum import Enum


class UndergroundStructureKind(Enum):
    """
    Kind of underground structure.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:17:13 PM
    """
    BURD = 1
    ENCLOSURE = 2
    HANDHOLE = 3
    MANHOLE = 4
    PAD = 5
    SUBSURFACE_ENCLOSURE = 6
    TRENCH = 7
    TUNNEL = 8
    VAULT = 9
    PULLBOX = 10
