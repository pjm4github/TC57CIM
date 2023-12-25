# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class LineDetail:
    def __init__(self):
        self.amount = Money()
        self.date_time = DateTime()
        self.note = ""
        self.rounding = Money()
