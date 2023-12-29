# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime


class LoadFollowingInst:
    """
    Metered SubSystem Load Following Instruction.

    @created 28-Dec-2023 5:22:00 PM
    """

    def __init__(self) -> None:
        self.end_time: Optional[DateTime] = DateTime()   # Instruction End Time
        self.load_following_mw: Optional[float] = 0.0  # Load Following MW Positive for follow-up and negative for follow-down
        self.mss_instruction_id: Optional[str] = ""  # Unique instruction id per instruction, assigned by the SC and provided to ADS. ADS passes through.
        self.start_time: Optional[DateTime] = DateTime()   # Instruction Start Time
