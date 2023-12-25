# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Agreement import Agreement
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.MerchantAccount import MerchantAccount


class MerchantAgreement(Agreement):
    """
    A formal controlling contractual agreement between supplier and merchant, in
    terms of which the merchant is authorised to vend tokens and receipt payments
    on behalf of the supplier. The merchant is accountable to the supplier for
    revenue collected at point of sale.
    @created 20-Dec-2023 5:07:58 PM
    """

    def __init__(self):
        super().__init__()
        self.merchant_accounts = MerchantAccount()
