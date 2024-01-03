package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.Flowgate;
import IEC62325.MarketCommon.MktGeneratingUnit;

/**
 * Optimal Power Flow or State Estimator Unit Data for Operator Training Simulator.
 * This is used for RealTime, Study and Maintenance Users.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class GeneratingUnitDynamicValues {

	/**
	 * Loss Factor
	 */
	public Float lossFactor;
	/**
	 * The maximum active power generation of the unit in MW
	 */
	public Float maximumMW;
	/**
	 * The minimum active power generation of the unit in MW
	 */
	public Float minimumMW;
	/**
	 * Unit reactive power generation in MVAR
	 */
	public Float mVAR;
	/**
	 * Unit active power generation in MW
	 */
	public Float mw;
	/**
	 * Unit sencivity factor. The distribution factors (DFAX) for the unit
	 */
	public Float sensitivity;
	public Flowgate Flowgate;
	public MktGeneratingUnit MktGeneratingUnit;

	public GeneratingUnitDynamicValues(){

	}
}//end GeneratingUnitDynamicValues