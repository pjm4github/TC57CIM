package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;

/**
 * Price of gas in monetary units.
 * @author USRAKHA
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class GasPrice {

	/**
	 * The average natural gas price at a defined fuel region.
	 */
	public Float gasPriceIndex;
	public FuelRegion FuelRegion;

	public GasPrice(){

	}
}//end GasPrice