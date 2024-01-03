package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;

/**
 * This class models the load distribution factors. This class should be used in
 * one of two ways:
 * 
 * Use it along with the AggregatedPnode and the IndividualPnode to show the
 * distriubtion of each individual party
 * 
 * OR
 * 
 * Use it with Mkt_EnergyConsumer to represent the current MW/Mvar distribution
 * within it's parnet load group.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class LoadDistributionFactor {

	/**
	 * Real power (MW) load distribution factor
	 */
	public Float pDistFactor;
	/**
	 * Reactive power (MVAr) load distribution factor
	 */
	public Float qDistFactor;

	public LoadDistributionFactor(){

	}
}//end LoadDistributionFactor