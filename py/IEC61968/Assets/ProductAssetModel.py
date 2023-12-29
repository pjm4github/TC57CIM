# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.InfIEC61968.InfAssetInfo.AssetModelCatalogueItem import AssetModelCatalogueItem
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ProductAssetModel(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.catalogue_number = ""
        self.corporate_standard_kind = ""
        self.drawing_number = ""
        self.instruction_manual = ""
        self.model_number = ""
        self.model_version = ""
        self.overall_length = Length()
        self.style_number = ""
        self.usage_kind = ""
        self.weight_total = ""
        self.asset_info = ""
        self.manufacturer = ""
        self.asset_model_catalogue_items = AssetModelCatalogueItem()
        self.catalog_asset_type = ""

