# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.Asset import Asset
from IEC61968.Common.Crew import Crew
from IEC61968.Work.MaterialItem import MaterialItem
from IEC61968.Work.WorkTaskKind import WorkTaskKind
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Hours import Hours
from IEC61970.Base.Domain.Money import Money


class WorkTask:
    def __init__(self):
        self.completed_date_time = DateTime()
        self.contractor_cost = Money()
        self.crew_eta = DateTime()
        self.instruction = ""
        self.labor_cost = Money()
        self.labor_hours = Hours()
        self.material_cost = Money()
        self.sched_override = ""
        self.started_date_time = DateTime()
        self.task_kind = WorkTaskKind.EXCHANGE
        self.tool_cost = Money()
        self.material_items = MaterialItem()
        self.old_asset = Asset()
        self.assets = Asset()
        self.crews = Crew()
