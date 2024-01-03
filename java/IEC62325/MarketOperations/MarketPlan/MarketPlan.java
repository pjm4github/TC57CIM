package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class identifies a set of planned markets.
 * @created 28-Dec-2023 8:12:12 PM
 */
public class MarketPlan extends IdentifiedObject {

	/**
	 * Planned market trading day.
	 */
	public DateTime tradingDay;
	/**
	 * A market plan has a number of markets (DA, HA, RT).
	 */
	public PlannedMarket PlannedMarket;

	public MarketPlan(){

	}
}//end MarketPlan