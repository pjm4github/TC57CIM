# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from IEC61968.Common.OrganisationRole import OrganisationRole
from IEC61968.Common.Status import Status


class BusinessRole(OrganisationRole):
    """
    A business role that this organisation plays. A single organisation typically
    performs many functions, each one described as a role.
    @created 29-Dec-2023 6:00:57 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.status: Status = Status()
        self.type: str = ""
