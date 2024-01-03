package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.Money;
import IEC61968.Common.Document;

/**
 * Provides pricing and other relevant information about a specific manufacturer's
 * product (i.e., AssetModel), and its price from a given supplier. A single
 * AssetModel may be availble from multiple suppliers. Note that manufacturer and
 * supplier are both types of organisation, which the association is inherited
 * from Document.
 * @created 29-Dec-2023 6:22:42 PM
 */
public class AssetModelCatalogueItem extends Document {

	/**
	 * Unit cost for an asset model from a specific supplier, either for a unit cost
	 * or cost per unit length. Cost is for material or asset only and does not
	 * include labor to install/construct or configure it.
	 */
	public Money unitCost;
	public ErpQuoteLineItem ErpQuoteLineItems;
	public ErpPOLineItem ErpPOLineItems;
	public AssetModelCatalogue AssetModelCatalogue;

	public AssetModelCatalogueItem(){

	}
}//end AssetModelCatalogueItem