package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.DateTime;

/**
 * Models Ancillary Service Requirements.  Describes interval for which the
 * requirement is applicable.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class ASRequirements {

	/**
	 * The start of the time interval for which requirement is defined.
	 */
	public DateTime intervalStartTime;
	public ReserveDemandCurve ReserveDemandCurve;

	public ASRequirements(){

	}
}//end ASRequirements