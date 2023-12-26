package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Boolean;

/**
 * Result of bid validation against conditions that may exist on an interchange
 * that becomes disconnected or is heavily discounted with respect the MW flow.
 * 
 * This schedule is assocated with the hourly parameters in a resource bid.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class OpenTieSchedule extends BidHourlySchedule {

	public Boolean value;

	public OpenTieSchedule(){

	}
}//end OpenTieSchedule