# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.Asset import Asset
from IEC61968.Common.Document import Document
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource


class OperationalTag(Document):
    
    def __init__(self):
        super().__init__()
        self.power_system_resource = PowerSystemResource()
        self.asset = Asset()
