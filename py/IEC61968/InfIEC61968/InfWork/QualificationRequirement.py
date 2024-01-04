# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfAssets.Specification import Specification
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class QualificationRequirement(WorkIdentifiedObject):
    """
    Certain skills are required and must be certified in order for a person
    (typically a member of a crew) to be qualified to work on types of equipment.
    @created 29-Dec-2023 9:18:10 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.qualification_id: Optional[str] = str()  # Qualification identifier.
        self.specifications: Optional[Specification] = Specification()
