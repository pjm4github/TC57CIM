# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

class CuContractorItem(WorkIdentifiedObject):
    """
    Compatible unit contractor item.
    """

    def __init__(self) -> None:
        self.activity_codeOptional[str] = None  # Activity code identifies a specific and distinguishable unit of work.
        self.bid_amountOptional[Money] = None  # The amount that a given contractor will charge for performing this unit of work.
        self.statusOptional[Status] = None
        self.compatible_unitsOptional[CompatibleUnit] = None
