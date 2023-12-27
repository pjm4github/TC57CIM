# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.PaymentMetering.AuxiliaryAccount import AuxiliaryAccount
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Money import Money

from IEC61968.Common.Agreement import Agreement

class AuxiliaryAgreement(Agreement):
    
    def __init__(self):
        super().__init__()
        self.arrears_interest = PerCent()
        self.aux_cycle = ""
        self.aux_priority_code = ""
        self.fixed_amount = Money()
        self.min_amount = Money()
        self.pay_cycle = ""
        self.sub_type = ""
        self.vend_portion = PerCent()
        self.vend_portion_arrear = PerCent()
        self.auxiliary_accounts = AuxiliaryAccount()
