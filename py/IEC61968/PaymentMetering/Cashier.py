# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ElectronicAddress import ElectronicAddress
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.CashierShift import CashierShift
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Cashier(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.electronic_address = ElectronicAddress()
        self.cashier_shifts = CashierShift()
