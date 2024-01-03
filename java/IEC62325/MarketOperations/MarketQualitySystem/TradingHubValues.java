package IEC62325.MarketOperations.MarketQualitySystem;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.AggregatedPnode;

/**
 * Models prices at Trading Hubs.
 * @created 03-Jan-2024 2:07:09 PM
 */
public class TradingHubValues {

	/**
	 * Utilizes the Market type. For DA, the price is hourly. For RTM the price is a 5
	 * minute price.
	 */
	public Float price;
	public AggregatedPnode AggregatedPnode;

	public TradingHubValues(){

	}
}//end TradingHubValues