# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.PaymentMetering.AccountMovement import AccountMovement
from IEC61968.PaymentMetering.Charge import Charge
from IEC61968.PaymentMetering.Due import Due
from IEC61968.PaymentMetering.Transaction import Transaction
from IEC61970.Base.Domain.Money import Money
from IEC61968.Common.Document import Document

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

        # Current amounts now due for payment on this account.

        self.due = Due()

        # Details of the last credit transaction performed on this account.
        self.last_credit = AccountMovement()

        # Details of the last debit transaction performed on this account.
        self.last_debit = AccountMovement()

        # The initial principal amount, with which this account was instantiated.
        self.principle_amount = Money()

        # All payments against this account.
        self.payment_transactions = Transaction()

        # All charges levied on this account.
        self.charges = Charge()
