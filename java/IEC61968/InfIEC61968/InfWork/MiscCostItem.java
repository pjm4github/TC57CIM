package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.IntegerQuantity;
import IEC61968.Common.Status;

/**
 * Various cost items that are not associated with compatible units. Examples
 * include rental equipment, labor, materials, contractor costs, permits -
 * anything not covered in a CU.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class MiscCostItem extends WorkIdentifiedObject {

	/**
	 * This drives the accounting treatment for this misc. item.
	 */
	public String account;
	/**
	 * The cost per unit for this misc. item.
	 */
	public Money costPerUnit;
	/**
	 * The cost type for accounting, such as material, labor, vehicle, contractor,
	 * equipment, overhead.
	 */
	public String costType;
	/**
	 * External reference identifier (e.g. purchase order number, serial number) .
	 */
	public String externalRefID;
	/**
	 * The quantity of the misc. item being assigned to this location.
	 */
	public IntegerQuantity quantity;
	public Status status;
	public WorkCostDetail WorkCostDetail;

	public MiscCostItem(){

	}
}//end MiscCostItem