package IEC62325.InfIEC62325.InfMarketResults;

import IEC61970.Base.Domain.Float;

/**
 * Provides the tie point specific output from the market applications. Currently,
 * this is defined as the loop flow compensation MW value.
 * @created 03-Jan-2024 1:54:12 PM
 */
public class InterTieResults {

	/**
	 * Net Actual MW Flow
	 */
	public Float baseMW;
	/**
	 * Net Dispatched MW
	 */
	public Float clearedValue;

	public InterTieResults(){

	}
}//end InterTieResults