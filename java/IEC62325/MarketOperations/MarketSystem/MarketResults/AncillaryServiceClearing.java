package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC62325.InfIEC62325.InfMarketResults.MarketCaseClearing;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Model of results of market clearing with respect to  Ancillary Service products.
 * 
 * @created 28-Dec-2023 8:18:19 PM
 */
public class AncillaryServiceClearing extends MarketFactors {

	public MarketRegionResults MarketRegionResults;
	public MarketCaseClearing MarketCaseClearing;

	public AncillaryServiceClearing(){

	}
}//end AncillaryServiceClearing