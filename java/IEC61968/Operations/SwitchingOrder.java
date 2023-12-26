package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61968.Common.Document;

/**
 * Transmits a switching plan to a crew in order for the plan to be executed.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchingOrder extends Document {

	/**
	 * Free-form comment associated with the switching order.
	 */
	public String comment;
	/**
	 * The planned start and end time for the switching order. 
	 */
	public DateTimeInterval plannedExecutionInterval;
	public SwitchingPlan SwitchingPlan;

	public SwitchingOrder(){

	}
}//end SwitchingOrder