package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61968.Common.Status;

/**
 * Compatible unit contractor item.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CUContractorItem extends WorkIdentifiedObject {

	/**
	 * Activity code identifies a specific and distinguishable unit of work.
	 */
	public String activityCode;
	/**
	 * The amount that a given contractor will charge for performing this unit of work.
	 */
	public Money bidAmount;
	public Status status;
	public CompatibleUnit CompatibleUnits;

	public CUContractorItem(){

	}
}//end CUContractorItem