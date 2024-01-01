# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from IEC61968.Common.OrganisationRole import OrganisationRole


class PersonOrganisationRole(OrganisationRole):
    """
    Role an organisation plays with respect to persons.
    @created 29-Dec-2023 6:02:18 PM
    """

    def __init__(self) -> None:
        """
        Identifiers of the person held by an organisation,
        such as a government agency (federal, state, province, city, county), financial institutions, etc.
        """
        super().__init__()
        self.client_id: str

