# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from IEC61968.Common.OrganisationRole import OrganisationRole


class OrgOrgRole(OrganisationRole):
    """Roles played between Organisations and other Organisations.
    
    This includes role ups for organisations, cost centers, profit centers, regulatory reporting, etc.
    
    Note that the parent and child relationship is indicated by the name on each end of the association.
    
    @created 29-Dec-2023 6:02:06 PM
    """

    def __init__(self) -> None:
        super().__init__()

        self.client_id = ""
