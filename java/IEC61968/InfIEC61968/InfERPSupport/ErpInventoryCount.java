import IEC61968.Common.Status;

/**
 * This is related to Inventory physical counts organized by AssetModel. Note that
 * a count of a type of asset can be accomplished by the association inherited by
 * AssetModel (from Document) to Asset.
 * It enables ERP applications to transfer an inventory count between ERP and the
 * actual physical inventory location. This count may be a cycle count or a
 * physical count.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpInventoryCount extends ErpIdentifiedObject {

	public Status status;

	public ErpInventoryCount(){

	}
}//end ErpInventoryCount