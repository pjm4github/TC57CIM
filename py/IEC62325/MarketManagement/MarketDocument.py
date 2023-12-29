# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Document import Document
from IEC62325.MarketManagement.AttributeInstanceComponent import AttributeInstanceComponent
from IEC62325.MarketManagement.Domain import Domain
from IEC62325.MarketManagement.Period import Period


class MarketDocument(Document):
    
    def __init__(self):
        super().__init__()
        self.self_market_document = MarketDocument()
        self.period = Period()
        self.attribute_instance_component = AttributeInstanceComponent()
        self.domain = Domain()
