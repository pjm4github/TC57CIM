# CashierShift.py
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.PointOfSale import PointOfSale
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Receipt import Receipt
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Shift import Shift
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Transaction import Transaction
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class CashierShift(Shift):
    """
    The operating shift for a cashier, during which the cashier may transact
    against the cashier shift, subject to vendor shift being open.
    """

    def __init__(self):
        super().__init__()
        self.cash_float = Money()  # The amount of cash that the cashier brings to start the shift and that will be taken away at the end of the shift; i.e. the cash float does not get banked.
        self.receipts = Receipt()  # All Receipts recorded for this Shift.
        self.point_of_sale = PointOfSale()  # Point of sale that is in operation during this shift.
        self.transactions = Transaction()  # All transactions recorded during this cashier shift.