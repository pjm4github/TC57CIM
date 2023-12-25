# analytic_score.py
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.Asset import Asset
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class AnalyticScore(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.calculation_date_time = DateTime()
        self.effective_date_time = DateTime()
        self.value = 0.0
        self.asset = Asset()

