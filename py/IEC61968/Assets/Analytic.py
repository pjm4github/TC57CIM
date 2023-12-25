# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AnalyticKind import AnalyticKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AnalyticScore import AnalyticScore
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.Asset import Asset
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetGroup import AssetGroup
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetHealthEvent import AssetHealthEvent
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.ScaleKind import ScaleKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common import Document

class Analytic(Document):
    
    def __init__(self):
        self.best_value = 0.0
        self.kind = AnalyticKind.OTHER
        self.scale_kind = ScaleKind.LINEAR
        self.worst_value = 0.0
        self.asset_group = AssetGroup()
        self.analytic_score = AnalyticScore()
        self.asset_health_event = AssetHealthEvent()
        self.asset = Asset()
