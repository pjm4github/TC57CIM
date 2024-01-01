# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Role(IdentifiedObject):
    """
    Enumeration of potential roles that might be played by one object relative to
    another.
    @created 29-Dec-2023 6:03:08 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.statusOptional[Status] = Status()
        """
        Type of role.
        """
        self.type: str = ""
