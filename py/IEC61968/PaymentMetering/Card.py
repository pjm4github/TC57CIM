# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106


from IEC61968.PaymentMetering.Tender import Tender
from IEC61970.Base.Domain.Date import Date


class Card:
    def __init__(self):
        self.account_holder_name = ""
        self.cv_number = ""
        self.expiry_date = Date()
        self.pan = ""
        self.tender = Tender()
