# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

class InterchangeETCData:
    """
    Existing Transmission Contract data for an interchange schedule.
    @created 27-Dec-2023 3:29:16 PM
    """

    def __init__(self) -> None:
        self.contract_number: Optional[str] = ""  # Existing transmission contract number
        self.usage_mw: float = 0.0  # Existing transmission contract usage MW value
