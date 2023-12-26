package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Core.RegularIntervalSchedule;

/**
 * Containment for bid hourly parameters that are not product dependent.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class BidHourlySchedule extends RegularIntervalSchedule {

	public Bid Bid;

	public BidHourlySchedule(){

	}
}//end BidHourlySchedule