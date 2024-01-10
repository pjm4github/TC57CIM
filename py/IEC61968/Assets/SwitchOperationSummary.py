# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.Asset import Asset
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Date import Date


class SwitchOperationSummary(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.lifetime_fault_operations = 0
        self.lifetime_motor_starts = 0
        self.lifetime_total_operations = 0
        self.most_recent_fault_operation_date = Date()
        self.most_recent_motor_start_date = Date()
        self.most_recent_operation_date = Date()
        self.breaker = Asset()
