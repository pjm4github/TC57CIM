package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.ReferenceData.PnodeDistributionFactor;

/**
 * This class allows SC to input different time intervals for distribution factors.
 * 
 * @created 28-Dec-2023 5:18:43 PM
 */
public class BidDistributionFactor {

	/**
	 * End of the time interval n which bid is valid (yyyy-mm-dd hh24: mi: ss) 
	 */
	public DateTime timeIntervalEnd;
	/**
	 * Start of the time interval in which bid is valid (yyyy-mm-dd hh24: mi: ss). 
	 */
	public DateTime timeIntervalStart;
	public PnodeDistributionFactor PnodeDistributionFactor;

	public BidDistributionFactor(){

	}
}//end BidDistributionFactor