# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfCommon.OldPerson import OldPerson
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Craft(IdentifiedObject):
    """
    Craft of a person or a crew. Examples include overhead electric, underground
    electric, high pressure gas, etc. This ensures necessary knowledge and skills
    before being allowed to perform certain types of work.
    @created 29-Dec-2023 6:01:16 PM
    """
    def __init__(self) -> None:
        super().__init__()
        """Classification by utility's work management standards and practices."""
        self.status = Status()
        self.type = ""
        self.erp_persons = OldPerson()
