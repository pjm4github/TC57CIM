# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.PaymentMetering.BankAccountDetail import BankAccountDetail
from IEC61968.PaymentMetering.ChequeKind import ChequeKind
from IEC61968.PaymentMetering.Tender import Tender
from IEC61970.Base.Domain.Date import Date


class Cheque:
    
    def __init__(self):
        self.bank_account_detail = BankAccountDetail()
        self.cheque_number = ""
        self.date = Date()
        self.kind = ChequeKind()
        self.micr_number = ""
        self.tender = Tender()
