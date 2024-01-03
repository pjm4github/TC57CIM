# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:37:42 2023
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class RedLine(IdentifiedObject):
    """
    This class is used for handling the accompanying annotations, time stamp,
    author, etc. of designs, drawings and maps. A red line can be associated with
    any Location object.
    @created 29-Dec-2023 6:06:52 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.status: Status = Status()
