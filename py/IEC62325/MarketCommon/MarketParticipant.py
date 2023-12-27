# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.ReferenceData.MarketPerson import MarketPerson

from IEC62325.MarketManagement.MarketDocument import MarketDocument

from IEC61968.Common.Organisation import Organisation

"""
An identification of a party acting in a electricity market business process.
This class is used to identify organizations that can participate in market
management and/or market operations.
@author T. Kostic
@version 1.0
@created 25-Dec-2023 9:21:22 PM
"""
class MarketParticipant(Organisation):
    def __init__(self):
        super().__init__()
        self.market_person = MarketPerson()
        self.market_document = MarketDocument()
