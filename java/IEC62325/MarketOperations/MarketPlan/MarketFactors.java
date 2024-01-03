package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Document;
import IEC62325.MarketOperations.MarketOpCommon.MktActivityRecord;

/**
 * Aggregation of market information relative for a specific time interval.
 * @created 28-Dec-2023 8:12:00 PM
 */
public class MarketFactors extends Document {

	/**
	 * The end of the time interval for which requirement is defined.
	 */
	public DateTime intervalEndTime;
	/**
	 * The start of the time interval for which requirement is defined.
	 */
	public DateTime intervalStartTime;
	public Market Market;
	public MktActivityRecord MktActivityRecord;

	public MarketFactors(){

	}
}//end MarketFactors