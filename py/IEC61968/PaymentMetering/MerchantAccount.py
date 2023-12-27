# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Document import Document
from IEC61968.PaymentMetering.Shift import Shift
from IEC61968.PaymentMetering.Transaction import Transaction
from IEC61970.Base.Domain.Money import Money


class MerchantAccount(Document):
    
    def __init__(self):
        super().__init__()
        self.current_balance = Money()
        self.provisional_balance = Money()
        self.transactors = Transaction()  # Assuming Transactor is a class
        self.vendor_shifts = Shift()  # Assuming VendorShift is a class
