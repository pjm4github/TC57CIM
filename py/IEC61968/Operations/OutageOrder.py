# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Document import Document
from IEC61968.Common.Location import Location


class OutageOrder(Document):
    
    def __init__(self):
        super().__init__()
        self.comment = ""
        self.location = Location()
