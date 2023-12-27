# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.Asset import Asset
from IEC61968.Common.Status import Status


class ErpItemMaster:
    
    def __init__(self):
        self.status = Status()
        self.asset = Asset()
