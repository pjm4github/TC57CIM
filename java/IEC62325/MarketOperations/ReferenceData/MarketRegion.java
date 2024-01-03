package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MarketSystem.MarketResults.MarketRegionResults;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.ReserveDemandCurve;

/**
 * A specialized class of AggregatedNode type. Defines the MarketRegions. Regions
 * could be system Market Regions, Energy Regions or Ancillary Service Regions.
 * @created 28-Dec-2023 12:17:33 PM
 */
public class MarketRegion extends AggregateNode {

	public MarketRegionResults MarketRegionResults;
	public ReserveDemandCurve ReserveDemandCurve;

	public MarketRegion(){

	}
}//end MarketRegion