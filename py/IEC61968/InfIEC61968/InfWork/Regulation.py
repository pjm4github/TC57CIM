# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument


class Regulation(WorkDocument):
    """
    Special requirements and/or regulations may pertain to certain types of assets
    or work. For example, fire protection and scaffolding.
    @created 29-Dec-2023 9:18:29 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.reference_number: Optional[str] = ""  # External reference to regulation, if applicable.
