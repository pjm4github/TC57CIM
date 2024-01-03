package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.MarketRegion;

/**
 * Model of expost calculation of cleared MW on a region basis.  Includes cleared
 * price.
 * @created 28-Dec-2023 8:20:38 PM
 */
public class ExPostMarketRegionResults {

	public Float exPostClearedPrice;
	public MarketRegion MarketRegion;
	public ExPostMarketRegion ExPostMarketRegion;

	public ExPostMarketRegionResults(){

	}
}//end ExPostMarketRegionResults