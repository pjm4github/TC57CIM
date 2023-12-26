import IEC61968.Common.Status;
import IEC61968.Assets.Asset;

/**
 * Any unique purchased part for manufactured product tracked by ERP systems for a
 * utility.
 * Item, as used by the OAG, refers to the basic information about an item,
 * including its attributes, cost, and locations. It does not include item
 * quantities. Compare to the Inventory, which includes all quantities and other
 * location-specific information.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpItemMaster extends ErpIdentifiedObject {

	public Status status;
	public Asset Asset;

	public ErpItemMaster(){

	}
}//end ErpItemMaster