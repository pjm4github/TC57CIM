# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Money import Money
from IEC61970.Base.Domain.DateTime import DateTime


class AccountMovement:
    
    def __init__(self):
        self.amount = Money()
        self.date_time = DateTime()
        self.reason = ""
