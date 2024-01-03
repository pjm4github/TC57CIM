package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MarketType;

/**
 * A containing class that groups all the distribution factors within a market.
 * 
 * This is calculated daily for DA factors and hourly for RT factors.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class DistributionFactorSet {

	/**
	 * The end of the time interval for which requirement is defined.
	 */
	public DateTime intervalEndTime;
	/**
	 * The start of the time interval for which requirement is defined.
	 */
	public DateTime intervalStartTime;
	/**
	 * Market type.
	 */
	public MarketType marketType;
	public GenDistributionFactor GenDistributionFactor;
	public SysLoadDistributionFactor SysLoadDistribuFactor;
	public LoadDistributionFactor LoadDistributionFactor;

	public DistributionFactorSet(){

	}
}//end DistributionFactorSet