package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Hours;
import IEC61970.Base.Domain.CostRate;
import IEC61968.Common.Status;

/**
 * Labor used for work order.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class LaborItem extends WorkIdentifiedObject {

	/**
	 * Activity code identifies a specific and distinguishable unit of work.
	 */
	public String activityCode;
	/**
	 * Total cost for labor. Note that this may not be able to be derived from labor
	 * rate and time charged.
	 */
	public Money cost;
	/**
	 * Time required to perform work.
	 */
	public Hours laborDuration;
	/**
	 * The labor rate applied for work.
	 */
	public CostRate laborRate;
	public Status status;
	public WorkCostDetail WorkCostDetail;

	public LaborItem(){

	}
}//end LaborItem