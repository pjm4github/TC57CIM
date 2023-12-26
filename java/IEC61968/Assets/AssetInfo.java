package IEC61968.Assets;

import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * Set of attributes of an asset, representing typical datasheet information of a
 * physical device that can be instantiated and shared in different data exchange
 * contexts:
 * - as attributes of an asset instance (installed or in stock)
 * - as attributes of an asset model (product by a manufacturer)
 * - as attributes of a type asset (generic type of an asset as used in
 * designs/extension planning).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AssetInfo extends IdentifiedObject {

	/**
	 * All power system resources with this datasheet information.
	 */
	public PowerSystemResource PowerSystemResources;
	public CatalogAssetType CatalogAssetType;

	public AssetInfo(){

	}
}//end AssetInfo