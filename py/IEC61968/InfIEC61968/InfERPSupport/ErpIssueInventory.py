# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.CatalogAssetType import CatalogAssetType
from IEC61968.Common.Status import Status


class ErpIssueInventory:

    def __init__(self):
        self.status = Status()
        self.type_material = TypeMaterial()
        self.type_asset = CatalogAssetType()
