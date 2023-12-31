# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61968.Assets.Asset import Asset
from IEC61968.Assets.AssetOwner import AssetOwner
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Ownership(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.share = PerCent()
        self.asset = Asset()
        self.asset_owner = AssetOwner()
