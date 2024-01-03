package IEC61968.Assets;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.StringQuantity;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61968.InfIEC61968.InfTypeAsset.TypeAssetCatalogue;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * assets that may be used for planning, work or design purposes.
 * @created 03-Jan-2024 12:03:38 PM
 */
public class CatalogAssetType extends IdentifiedObject {

	/**
	 * Estimated unit cost (or cost per unit length) of this type of asset. It does
	 * not include labor to install, construct or configure it.
	 */
	public Money estimatedUnitCost;
	public AssetKind kind;
	/**
	 * The value, unit of measure, and multiplier for the quantity.
	 */
	public StringQuantity quantity;
	/**
	 * True if item is a stock item (default).
	 */
	public Boolean stockItem;
	public String type;
	public TypeAssetCatalogue TypeAssetCatalogue;
	public ErpReqLineItem ErpReqLineItems;
	public ErpBomItemData ErpBomItemDatas;

	public CatalogAssetType(){

	}
}//end CatalogAssetType