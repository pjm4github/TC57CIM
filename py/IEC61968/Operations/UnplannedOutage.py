# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Customers.TroubleTicket import TroubleTicket
from IEC61968.Operations.Outage import Outage
from IEC61968.Operations.OutageCauseKind import OutageCauseKind
from IEC61970.Base.Domain.DateTime import DateTime


class UnplannedOutage(Outage):
    
    def __init__(self):
        super().__init__()
        self.cause = ""
        self.cause_kind = OutageCauseKind()
        self.reported_start_time = DateTime()
        self.trouble_ticket = TroubleTicket()
