package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MarketType;

/**
 * Represent a planned market. For example a planned DA/HA/RT market.
 * @created 28-Dec-2023 8:12:40 PM
 */
public class PlannedMarket {

	/**
	 * Market end time.
	 */
	public DateTime marketEndTime;
	/**
	 * Market start time.
	 */
	public DateTime marketStartTime;
	/**
	 * Market type.
	 */
	public MarketType marketType;
	/**
	 * A planned market could have multiple market runs for the reason that a planned
	 * market could have a rerun.
	 */
	public MarketRun MarketRun;
	/**
	 * A planned market shall have a set of planned events
	 */
	public PlannedMarketEvent PlannedMarketEvent;

	public PlannedMarket(){

	}
}//end PlannedMarket