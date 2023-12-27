# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Operations.ERTConfidenceKind import ERTConfidenceKind
from IEC61968.Operations.Outage import Outage
from IEC61970.Base.Domain.DateTime import DateTime


class EstimatedRestorationTime:
    
    def __init__(self):
        self.confidence_kind = ERTConfidenceKind.HIGH
        self.ert = DateTime()
        self.ert_source = ""
        self.outage = Outage()
