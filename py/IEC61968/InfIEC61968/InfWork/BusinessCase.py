# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfWork.Project import Project
from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61968.Work.Work import Work


class BusinessCase(WorkDocument):
    """
    Business justification for capital expenditures, usually addressing operations
    and maintenance costs as well.
    @created 29-Dec-2023 9:11:09 PM
    """

    def __init__(self) -> None:
        super().__init__()
        """
        A codified representation of the business case (i.e., codes for highway
        relocation, replace substation transformers, etc.).
        """
        self.corporate_code = ""
        self.projects = Project()
        self.works = [Work()]
