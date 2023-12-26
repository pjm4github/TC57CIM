import IEC61968.Common.Status;

/**
 * Utility inventory-related information about an item or part (and not for
 * description of the item and its attributes). It is used by ERP applications to
 * enable the synchronization of Inventory data that exists on separate Item
 * Master databases. This data is not the master data that describes the
 * attributes of the item such as dimensions, weight, or unit of measure - it
 * describes the item as it exists at a specific location.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpInventory extends ErpIdentifiedObject {

	public Status status;

	public ErpInventory(){

	}
}//end ErpInventory