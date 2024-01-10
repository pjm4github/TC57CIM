# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Local imports
from IEC62325.MarketManagement.MarketDocument import MarketDocument
from IEC62325.MarketManagement.Unit import Unit


# The Area Control Error tariff type that is applied or used.
# @author mspivbe2
# @version 1.0
# @created 25-Dec-2023 9:21:21 PM
class AceTariffType:
    
    # The coded type of ACE tariff.
    def __init__(self):
        self.type = ""
        self.unit = Unit()
        self.market_document = MarketDocument()
