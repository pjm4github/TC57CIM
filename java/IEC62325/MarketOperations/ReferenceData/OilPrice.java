package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;

/**
 * Price of oil in monetary units.
 * @author USRAKHA
 * @version 1.0
 * @created 25-Dec-2023 9:21:23 PM
 */
public class OilPrice {

	/**
	 * The average oil price at a defined fuel region.
	 */
	public Float oilPriceIndex;
	public FuelRegion FuelRegion;

	public OilPrice(){

	}
}//end OilPrice