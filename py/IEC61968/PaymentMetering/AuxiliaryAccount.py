# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.AccountMovement import AccountMovement
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Charge import Charge
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Due import Due
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Transaction import Transaction
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document

"""
Variable and dynamic part of auxiliary agreement, generally representing the
current state of the account related to the outstanding balance defined in
auxiliary agreement.
@created 20-Dec-2023 5:05:28 PM
"""
class AuxiliaryAccount(Document):

    """
    The total amount currently remaining on this account that is required to be
    paid in order to settle the account to zero. This excludes any due amounts
    not yet paid.
    """
    def __init__(self):
        super().__init__()
        self.balance = Money()

    """
    Current amounts now due for payment on this account.
    """
    def due(self):
        self.due = Due()

    """
    Details of the last credit transaction performed on this account.
    """
    def last_credit(self):
        self.last_credit = AccountMovement()

    """
    Details of the last debit transaction performed on this account.
    """
    def last_debit(self):
        self.last_debit = AccountMovement()

    """
    The initial principle amount, with which this account was instantiated.
    """
    def principle_amount(self):
        self.principle_amount = Money()

    """
    All payments against this account.
    """
    def payment_transactions(self):
        self.payment_transactions = Transaction()

    """
    All charges levied on this account.
    """
    def charges(self):
        self.charges = Charge()
