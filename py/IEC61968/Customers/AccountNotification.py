# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class AccountNotification:
    def __init__(self):
        self.customer_notification_type = ""
        self.method_type = ""
        self.note = ""
        self.time = DateTime()
