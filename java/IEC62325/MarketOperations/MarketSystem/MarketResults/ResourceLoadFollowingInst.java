package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * Model of market clearing results for resources that bid to follow load.
 * @created 28-Dec-2023 8:26:04 PM
 */
public class ResourceLoadFollowingInst {

	/**
	 * weighted average for RTPD and RTCD and same for RTID
	 */
	public Float calcLoadFollowingMW;
	public Float dispWindowHighLimt;
	public Float dispWindowLowLimt;
	/**
	 * Unique instruction id per instruction, assigned by the SC and provided to ADS.
	 * ADS passes through.
	 */
	public String instructionID;
	/**
	 * The start of the time interval for which requirement is defined.
	 */
	public DateTime intervalStartTime;

	public ResourceLoadFollowingInst(){

	}
}//end ResourceLoadFollowingInst