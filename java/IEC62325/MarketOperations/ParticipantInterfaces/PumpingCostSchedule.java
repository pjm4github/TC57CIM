package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Float;

/**
 * The operating cost of a Pump Storage Hydro Unit operating as a hydro pump.
 * 
 * This schedule is assocated with the hourly parameters in a resource bid
 * associated with a specific product within the bid.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class PumpingCostSchedule extends BidHourlyProductSchedule {

	public Float value;

	public PumpingCostSchedule(){

	}
}//end PumpingCostSchedule