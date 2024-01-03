package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Model of ex-post pricing of nodes.
 * @created 28-Dec-2023 8:20:46 PM
 */
public class ExPostPricing extends MarketFactors {

	/**
	 * market energy price
	 */
	public Float energyPrice;

	public ExPostPricing(){

	}
}//end ExPostPricing