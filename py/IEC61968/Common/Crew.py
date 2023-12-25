# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Crew(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.status = None  # Status of this crew.
        self.crew_type = None  # Type of this crew.
        self.crew_members = None  # All members of this crew.
