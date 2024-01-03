package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61968.Common.Status;

/**
 * Contractor information for work task.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class ContractorItem extends WorkIdentifiedObject {

	/**
	 * Activity code identifies a specific and distinguishable unit of work.
	 */
	public String activityCode;
	/**
	 * The amount that a given contractor will charge for performing this unit of work.
	 */
	public Money bidAmount;
	/**
	 * The total amount charged.
	 */
	public Money cost;
	public Status status;
	public ErpPayable ErpPayables;

	public ContractorItem(){

	}
}//end ContractorItem