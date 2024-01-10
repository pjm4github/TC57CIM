# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:37:42 2023
from IEC61968.Common.Location import Location
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Route(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.status = Status()  # Classification by utility's work management standards and practices
        self.type: str = ""  # Classification by utility's work management standards and practices
        self.locations = [Location()]
