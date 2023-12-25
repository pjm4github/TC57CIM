# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.CatalogAssetType import CatalogAssetType
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PowerSystemResource import PowerSystemResource


class AssetInfo(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.power_system_resources = PowerSystemResource()
        self.catalog_asset_type = CatalogAssetType()
