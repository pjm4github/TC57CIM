package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC62325.MarketOperations.MktDomain.PriceTypeKind;

/**
 * The price of a Commodity during a given time interval may change over time.
 * For example, a price may be forecasted a year ahead, a month ahead, a day ahead,
 * an hour ahead, and in real time; this is defined using the MarketType.
 * Additionally a price may have one or more components. For example, a locational
 * marginal energy price may be the arithmetic sum of the system price, the
 * congestion price, and the loss price.  The priceType enumeration is used
 * determine if the price is the complete price (priceType="total") or one of
 * potentially many constituent components.
 * @author Margaret
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class PriceDescriptor {

	/**
	 * The time frame for the price, using the standard conventions associated with
	 * the MarketType enumeration.
	 */
	public MarketType marketType;
	/**
	 * The "kind" of price being described.  In general, the priceType will either be
	 * "total" to signify that the price is the price paid to buy or sell the
	 * commodity, sometimes referred to as an "all-in" price, or one of potentially
	 * many components.
	 */
	public PriceTypeKind priceType;

	public PriceDescriptor(){

	}
}//end PriceDescriptor