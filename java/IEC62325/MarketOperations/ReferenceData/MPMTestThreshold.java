package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.CostPerEnergyUnit;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Market Power Mitigation (MPM) test thresholds for resource as well as
 * designated congestion areas (DCAs).
 * @created 28-Dec-2023 12:16:22 PM
 */
public class MPMTestThreshold {

	/**
	 * Market Type (DAM, RTM)
	 */
	public MarketType marketType;
	/**
	 * Price Threshold in %
	 */
	public PerCent percent;
	/**
	 * Price Threshold in $/MW
	 */
	public CostPerEnergyUnit price;
	public AggregatedPnode AggregatedPnode;
	public RegisteredResource RegisteredResource;

	public MPMTestThreshold(){

	}
}//end MPMTestThreshold