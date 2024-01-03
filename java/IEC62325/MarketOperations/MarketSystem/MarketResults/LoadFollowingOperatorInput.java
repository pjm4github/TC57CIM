package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Model of load following capabilities that are entered by operators on a
 * temporary basis.  Related to Registered Resources in Metered Subsystems.
 * @created 28-Dec-2023 8:22:10 PM
 */
public class LoadFollowingOperatorInput {

	/**
	 * Time the data entry was performed
	 */
	public DateTime dataEntryTimeStamp;
	/**
	 * temporarily manually entered LFD capacity
	 */
	public Float tempLoadFollowingDownManualCap;
	/**
	 * temporarily manually entered LFU capacity.
	 */
	public Float tempLoadFollowingUpManualCap;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;
	public RegisteredResource RegisteredResource;

	public LoadFollowingOperatorInput(){

	}
}//end LoadFollowingOperatorInput