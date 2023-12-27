# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Work.BreakerRepairItemKind import BreakerRepairItemKind
from IEC61968.Work.RepairWorkTask import RepairWorkTask
from IEC61968.Work.TransformerRepairItemKind import TransformerRepairItemKind


class RepairItem:
    
    def __init__(self):
        self.breaker_repair_item = BreakerRepairItemKind.OTHER
        self.transformer_repair_item = TransformerRepairItemKind.NOTHING
        self.repair_work_task = RepairWorkTask()
