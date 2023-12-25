# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class FieldDispatchStep:
    def __init__(self):
        self.dispatch_status = Status()  # The status of one or more crews dispatched to perform field work at one or more work sites
        self.occurred_date_time = DateTime()  # The date and time at which the dispatch status occurred
        self.remarks = ""  # Freeform comments related to the dispatch to perform field work
        self.sequence_number = 0  # The sequence number of the field dispatch step within the field dispatch history. Begins with 1 and increments up
