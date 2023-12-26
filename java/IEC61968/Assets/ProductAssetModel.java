package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Length;
import IEC61968.InfIEC61968.InfAssetInfo.AssetModelCatalogueItem;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Asset model by a specific manufacturer.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ProductAssetModel extends IdentifiedObject {

	/**
	 * Catalogue number for asset model.
	 */
	public String catalogueNumber;
	/**
	 * Kind of corporate standard for this asset model.
	 */
	public CorporateStandardKind corporateStandardKind;
	/**
	 * Drawing number for asset model.
	 */
	public String drawingNumber;
	/**
	 * Reference manual or instruction book for this asset model.
	 */
	public String instructionManual;
	/**
	 * Manufacturer's model number.
	 */
	public String modelNumber;
	/**
	 * Version number for product model, which indicates vintage of the product.
	 */
	public String modelVersion;
	/**
	 * Overall length of this asset model.
	 */
	public Length overallLength;
	/**
	 * Style number of asset model.
	 */
	public String styleNumber;
	/**
	 * Intended usage for this asset model.
	 */
	public AssetModelUsageKind usageKind;
	/**
	 * Total manufactured weight of asset.
	 */
	public Mass weightTotal;
	public AssetInfo AssetInfo;
	/**
	 * Manufacturer of this asset model.
	 */
	public Manufacturer Manufacturer;
	public AssetModelCatalogueItem AssetModelCatalogueItems;
	public CatalogAssetType CatalogAssetType;

	public ProductAssetModel(){

	}
}//end ProductAssetModel