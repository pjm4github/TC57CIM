# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class Shift(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.activity_interval = DateTimeInterval()
        self.receipts_grand_total_bankable = Money()
        self.receipts_grand_total_non_bankable = Money()
        self.receipts_grand_total_rounding = Money()
        self.transactions_grand_total = Money()
        self.transactions_grand_total_rounding = Money()
