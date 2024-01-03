package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Status;

/**
 * This is to specify the various condition factors for a design that may alter
 * the cost estimate or the allocation.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class ConditionFactor extends WorkIdentifiedObject {

	/**
	 * The actual value of the condition factor, such as labor flat fee or percentage.
	 */
	public String cfValue;
	/**
	 * Kind of this condition factor.
	 */
	public ConditionFactorKind kind;
	public Status status;

	public ConditionFactor(){

	}
}//end ConditionFactor