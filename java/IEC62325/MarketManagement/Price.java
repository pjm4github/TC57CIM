package IEC62325.MarketManagement;

import IEC61970.Base.Domain.Decimal;
import IEC61970.Base.Domain.String;

/**
 * The cost corresponding to a specific measure and expressed in a currency.
 * @author effantin-cyr
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class Price {

	/**
	 * A number of monetary units specified in a unit of currency.
	 */
	public Decimal amount;
	/**
	 * The category of a price to be used in a price calculation. The price category
	 * is mutually agreed between System Operators.
	 */
	public String category;
	/**
	 * The direction indicates whether a System Operator pays the Market Parties or
	 * inverse.
	 */
	public String direction;
	public Point Point;
	public TimeSeries TimeSeries;
	public Domain Domain;

	public Price(){

	}
}//end Price