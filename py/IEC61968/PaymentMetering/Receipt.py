# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.PaymentMetering.LineDetail import LineDetail
from IEC61968.PaymentMetering.Transaction import Transaction
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Receipt(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.is_bankable = True
        self.line = LineDetail()
        self.transactions = Transaction()
