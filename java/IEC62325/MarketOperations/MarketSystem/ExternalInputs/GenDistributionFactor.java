package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;

/**
 * This class models the generation distribution factors. This class needs to be
 * used along with the AggregatedPnode and the IndividualPnode to show the
 * distribution of each individual party.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class GenDistributionFactor {

	/**
	 * Used to calculate generation "participation" of an individual pnond in an
	 * AggregatePnode. 
	 */
	public Float factor;

	public GenDistributionFactor(){

	}
}//end GenDistributionFactor