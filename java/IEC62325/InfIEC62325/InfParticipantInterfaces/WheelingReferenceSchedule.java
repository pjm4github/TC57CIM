package IEC62325.InfIEC62325.InfParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.ParticipantInterfaces.BidHourlySchedule;

/**
 * A unique identifier of a wheeling transaction. A wheeling transaction is a
 * balanced Energy exchange among Supply and Demand Resources.
 * 
 * This schedule is assocated with the hourly parameters in a resource bid.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class WheelingReferenceSchedule extends BidHourlySchedule {

	public String value;

	public WheelingReferenceSchedule(){

	}
}//end WheelingReferenceSchedule