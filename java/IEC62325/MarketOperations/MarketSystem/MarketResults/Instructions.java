package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MktDomain.MQSInstructionSource;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.AutomaticDispInstTypeCommitment;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.ReferenceData.AggregateNode;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Provides the necessary information (on a resource basis) to capture the
 * Startup/Shutdown instruction results. This information is relevant to the DA
 * Market (RUC only) as well as the RT Market (HASP, Pre-dispatch, and Interval).
 * @created 28-Dec-2023 8:22:03 PM
 */
public class Instructions {

	/**
	 * Binding dispatch operating delta provides a relative delta to be applied.
	 * Typically used in demand response instructions. The binding<font
	 * color="#0f0f0f">DOD instructions are cumulative; in other words a second DOD
	 * instruction does not replace the previous DOD, instead the second DOD adds to
	 * the previous DODs.</font>
	 */
	public Float bindingDOD;
	public Float bindingDOT;
	public YesNo bindingInstruction;
	/**
	 * Total cost associated with changing the status of the resource.
	 */
	public Float instructionCost;
	/**
	 * instruction source for market quality results (INS, ACT)
	 */
	public MQSInstructionSource instructionSource;
	/**
	 * Time the resource should be at Pmin (for start ups).
	 * 
	 * Time the resource is off line.
	 */
	public DateTime instructionStartTime;
	/**
	 * Indicator of either a Start-Up or a Shut-Down.
	 */
	public AutomaticDispInstTypeCommitment instructionType;
	/**
	 * Manually Blocked Indicator (Yes/No). The instruction has been blocked by an
	 * Operator.
	 */
	public YesNo manuallyBlocked;
	/**
	 * Minimum start up time required to bring the unit online (minutes).
	 * 
	 * SCUC commitment period start-up time. Calculated start up time based on the
	 * StartUpTimeCurve provided with the Bid.
	 * 
	 * This is a combination of StartUp time bid and Unit down time.
	 * 
	 * Units is minutes
	 */
	public Integer minStatusChangeTime;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;
	public InstructionClearing InstructionClearing;
	public AggregateNode AggregateNode;
	public RegisteredResource RegisteredResource;

	public Instructions(){

	}
}//end Instructions