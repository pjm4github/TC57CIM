# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.AreaKind import AreaKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.Outage import Outage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class OutageArea:
    def __init__(self):
        self.earliest_reported_time = DateTime()
        self.meters_served = 0
        self.outage_area_kind = AreaKind.SERVICE_AREA
        self.outage = Outage()
