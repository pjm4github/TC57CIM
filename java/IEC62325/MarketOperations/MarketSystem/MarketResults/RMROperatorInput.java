package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * RMR Operator's entry of the RMR requirement per market interval.
 * @created 28-Dec-2023 8:25:02 PM
 */
public class RMROperatorInput extends MarketFactors {

	/**
	 * The lower of the original pre-dispatch or the AC run schedule (Also known as
	 * the RMR Reguirement) becomes the pre-dispatch value. 
	 */
	public Float manuallySchedRMRMw;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;

	public RMROperatorInput(){

	}
}//end RMROperatorInput