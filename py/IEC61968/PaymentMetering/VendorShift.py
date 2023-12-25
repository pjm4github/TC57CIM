# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Receipt import Receipt
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Shift import Shift
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Transaction import Transaction
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class VendorShift(Shift):
    
    def __init__(self):
        super().__init__()
        # 	 * The amount that is to be debited from the merchant account for this vendor
        # 	 * shift. This amount reflects the sum(PaymentTransaction.transactionAmount).
        self.merchant_debit_amount = Money()
        # 	 * If true, merchantDebitAmount has been debited from MerchantAccount; typically
        # 	 * happens at the end of VendorShift when it closes.
        self.posted = False
        # 	 * All receipts recorded during this vendor shift.
        self.receipts = [Receipt()]
        # 	 * All transactions recorded during this vendor shift.
        self.transactions = [Transaction()]
