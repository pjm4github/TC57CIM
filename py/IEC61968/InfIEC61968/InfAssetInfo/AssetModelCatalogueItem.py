# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Any

from IEC61968.Common.Document import Document
from IEC61968.InfIEC61968.InfAssetInfo.AssetModelCatalogue import AssetModelCatalogue
from IEC61968.InfIEC61968.InfERPSupport.ErpPOLineItem import ErpPOLineItem
from IEC61968.InfIEC61968.InfERPSupport.ErpQuoteLineItem import ErpQuoteLineItem
from IEC61970.Base.Domain.Money import Money


class AssetModelCatalogueItem(Document):
    """Provides pricing and other relevant information about a specific manufacturer's
    product (i.e., AssetModel), and its price from a given supplier. A single
    AssetModel may be availble from multiple suppliers. Note that manufacturer and
    supplier are both types of organisation, which the association is inherited
    from Document.
    @created 29-Dec-2023 6:22:42 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.unit_cost: Money = Money(0.00)
        self.erp_quote_line_items: ErpQuoteLineItem = ErpQuoteLineItem()
        self.erp_po_line_items: ErpPOLineItem = ErpPOLineItem()
        self.asset_model_catalogue: AssetModelCatalogue = AssetModelCatalogue()
