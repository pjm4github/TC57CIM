package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Boolean;

/**
 * An indicator specifying that a resource shall have an Hourly Pre-Dispatch. The
 * resource could be a RegisteredGenerator or a RegisteredInterTie.
 * 
 * This schedule is assocated with the hourly parameters in a resource bid.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class HourlyPreDispatchSchedule extends BidHourlySchedule {

	/**
	 * Flag defining that for this hour in the resource bid the resource shall have an
	 * hourly pre-dispatch.
	 */
	public Boolean value;

	public HourlyPreDispatchSchedule(){

	}
}//end HourlyPreDispatchSchedule