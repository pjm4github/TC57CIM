# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.AnalyticKind import AnalyticKind
from IEC61968.Assets.AnalyticScore import AnalyticScore
from IEC61968.Assets.Asset import Asset
from IEC61968.Assets.AssetGroup import AssetGroup
from IEC61968.Assets.AssetHealthEvent import AssetHealthEvent
from IEC61968.Assets.ScaleKind import ScaleKind
from IEC61968.Common import Document


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
