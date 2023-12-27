# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Work.BreakerMaintenanceKind import BreakerMaintenanceKind
from IEC61968.Work.TransformerMaintenanceKind import TransformerMaintenanceKind
from IEC61968.Work.WorkTask import WorkTask


class MaintenanceWorkTask(WorkTask):
    
    def __init__(self):
        super().__init__()
        self.breaker_maintenance_kind = BreakerMaintenanceKind.INTERRUPTER_OVERHAUL
        self.transformer_maintenance_kind = TransformerMaintenanceKind.NOTHING
