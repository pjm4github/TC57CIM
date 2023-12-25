from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetKind import AssetKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpBomItemData import ErpBomItemData
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpReqLineItem import ErpReqLineItem
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfTypeAsset.TypeAssetCatalogue import TypeAssetCatalogue
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class CatalogAssetType(IdentifiedObject):
    """
    assets that may be used for planning, work or design purposes.
    """

    def __init__(self):
        """
        Constructor for CatalogAssetType.
        """
        super().__init__()
        self.estimatedUnitCost = Money()
        """
        Estimated unit cost (or cost per unit length) of this type of asset. It does
        not include labor to install, construct or configure it.
        """

        self.kind = AssetKind.OTHER
        """
        The kind of asset.
        """

        self.quantity = "0"
        """
        The value, unit of measure, and multiplier for the quantity.
        """

        self.stockItem = True
        """
        True if item is a stock item (default).
        """

        self.type = ""
        """
        The type of asset.
        """

        self.TypeAssetCatalogue = TypeAssetCatalogue()
        """
        The asset catalogue type.
        """

        self.ErpReqLineItems = ErpReqLineItem()
        """
        The ERP request line items.
        """

        self.ErpBomItemDatas = ErpBomItemData()
        """
        The ERP BOM item datas.
        """
