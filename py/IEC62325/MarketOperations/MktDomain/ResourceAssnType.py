# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class ResourceAssnType(Enum):
    """
    For example:
    Asset Owner Sink designator for use by CRR
    Asset Owner Source designator for use by CRR
    Reliability Must Run
    Scheduling Coordinator
    Load Serving Entity
    """
    CSNK = 1
    CSRC = 2
    RMR = 3
    SC = 4
    LSE = 5
