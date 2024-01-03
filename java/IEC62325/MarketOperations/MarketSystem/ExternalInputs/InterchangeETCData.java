package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Float;

/**
 * Existing Transmission Contract data for an interchange schedule.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class InterchangeETCData {

	/**
	 * Existing transmission contract number
	 */
	public String contractNumber;
	/**
	 * Existing transmission contract usage MW value
	 */
	public Float usageMW;

	public InterchangeETCData(){

	}
}//end InterchangeETCData