# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.InfIEC61968.InfAssetInfo.AssetModelCatalogueItem import AssetModelCatalogueItem
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ProductAssetModel(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.catalogue_number = str()
        self.corporate_standard_kind = str()
        self.drawing_number = str()
        self.instruction_manual = str()
        self.model_number = str()
        self.model_version = str()
        self.overall_length = Length()
        self.style_number = str()
        self.usage_kind = str()
        self.weight_total = str()
        self.asset_info = str()
        self.manufacturer = str()
        self.asset_model_catalogue_items = AssetModelCatalogueItem()
        self.catalog_asset_type = str()

