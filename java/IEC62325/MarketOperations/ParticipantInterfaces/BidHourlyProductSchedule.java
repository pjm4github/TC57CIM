package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Core.RegularIntervalSchedule;

/**
 * Containment for bid parameters that are dependent on a market product type.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class BidHourlyProductSchedule extends RegularIntervalSchedule {

	public ProductBid ProductBid;

	public BidHourlyProductSchedule(){

	}
}//end BidHourlyProductSchedule