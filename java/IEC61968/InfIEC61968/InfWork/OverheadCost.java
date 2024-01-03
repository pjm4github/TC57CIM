package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61968.Common.Status;

/**
 * Overhead cost applied to work order.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class OverheadCost extends WorkIdentifiedObject {

	/**
	 * Overhead code.
	 */
	public String code;
	/**
	 * The overhead cost to be applied.
	 */
	public Money cost;
	public Status status;
	public WorkCostDetail WorkCostDetails;

	public OverheadCost(){

	}
}//end OverheadCost