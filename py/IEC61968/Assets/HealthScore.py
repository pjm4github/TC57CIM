# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.AggregateScore import AggregateScore
from IEC61968.Assets.RiskScore import RiskScore


class HealthScore(AggregateScore):
    
    def __init__(self):
        super().__init__()
        self.asset_risk_score = RiskScore()
