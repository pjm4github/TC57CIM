
from IEC61968.Common.OrganisationRole import OrganisationRole
from IEC62325.MarketCommon.MarketParticipant import MarketParticipant


class MarketRole(OrganisationRole):
    def __init__(self):
        super().__init__()
        self.type = ""# Creating an instance of String class and assigning it to the 'type' attribute
        self.MarketParticipant = MarketParticipant() # Creating an instance of MarketParticipant class and assigning it to the 'MarketParticipant' attribute
