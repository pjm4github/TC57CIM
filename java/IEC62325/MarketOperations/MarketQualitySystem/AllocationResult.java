package IEC62325.MarketOperations.MarketQualitySystem;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;

/**
 * Models Market clearing results.  Indicates market horizon, interval based. Used
 * by a market quality system for billing and settlement purposes.
 * @created 03-Jan-2024 2:07:09 PM
 */
public class AllocationResult {

	public DateTime intervalStartTime;
	public DateTime updateTimeStamp;
	public String updateUser;
	public AllocationResultValues AllocationResultValues;

	public AllocationResult(){

	}
}//end AllocationResult