# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfCommon.OldPerson import OldPerson
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Craft(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.status: Status = Status()
        """Classification by utility's work management standards and practices."""
        self.type: str
        self.erp_personsOptional[OldPerson] = OldPerson()
