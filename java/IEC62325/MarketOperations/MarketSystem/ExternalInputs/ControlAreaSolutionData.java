package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;

/**
 * State Estimator Solution Pool Interchange and Losses.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class ControlAreaSolutionData {

	/**
	 * Pool MW Interchange
	 * Attribute Usage: The active power interchange of the pool
	 */
	public Float solvedInterchange;
	/**
	 * Pool Losses MW
	 * Attribute Usage: The active power losses of the pool in MW
	 */
	public Float solvedLosses;
	public MktControlArea MktControlArea;

	public ControlAreaSolutionData(){

	}
}//end ControlAreaSolutionData