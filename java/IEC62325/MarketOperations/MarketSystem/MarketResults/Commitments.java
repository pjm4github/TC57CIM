package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC62325.MarketOperations.MktDomain.CommitmentType;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.AutomaticDispInstTypeCommitment;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;

/**
 * Provides the necessary information (on a resource basis) to capture the
 * Startup/Shutdown commitment results. This information is relevant to all
 * markets.
 * @created 28-Dec-2023 8:19:10 PM
 */
public class Commitments {

	/**
	 * the type of UC status (self commitment, ISO commitment, or SCUC commitment)
	 */
	public CommitmentType commitmentType;
	/**
	 * Total cost associated with changing the status of the resource.
	 */
	public Float instructionCost;
	/**
	 * Indicator of either a Start-Up or a Shut-Down.
	 */
	public AutomaticDispInstTypeCommitment instructionType;
	/**
	 * End time for the commitment period. This will be on an interval boundary.
	 */
	public DateTime intervalEndTime;
	/**
	 * Start time for the commitment period. This will be on an interval boundary.
	 */
	public DateTime intervalStartTime;
	/**
	 * SCUC commitment period start-up time. Calculated start up time based on the
	 * StartUpTimeCurve provided with the Bid.
	 * 
	 * This is a combination of StartUp time bid and Unit down time.
	 * 
	 * Units is minutes
	 */
	public Integer minStatusChangeTime;
	/**
	 * Unit no load cost in case of energy commodity
	 */
	public Float noLoadCost;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;

	public Commitments(){

	}
}//end Commitments