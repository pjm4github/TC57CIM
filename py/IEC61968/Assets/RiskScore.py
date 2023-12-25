# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# risk_score.py
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AggregateScore import AggregateScore


class RiskScore(AggregateScore):
    def __init__(self):
        super().__init__()
        self.kind = None
