# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.PaymentMetering.Receipt import Receipt
from IEC61968.PaymentMetering.TenderKind import TenderKind
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Money import Money


class Tender(IdentifiedObject):
   
    def __init__(self):
        super().__init__()
        self.amount = Money()
        self.change = Money()
        self.kind = TenderKind.CASH
        self.receipt = Receipt()
