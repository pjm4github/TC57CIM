package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;

/**
 * Metered SubSystem Load Following Instruction.
 * @created 28-Dec-2023 5:22:00 PM
 */
public class LoadFollowingInst {

	/**
	 * Instruction End Time
	 */
	public DateTime endTime;
	/**
	 * Load Following MW Positive for follow-up and negative for follow-down
	 */
	public Float loadFollowingMW;
	/**
	 * Unique instruction id per instruction, assigned by the SC and provided to ADS.
	 * ADS passes through.
	 */
	public String mssInstructionID;
	/**
	 * Instruction Start Time
	 */
	public DateTime startTime;

	public LoadFollowingInst(){

	}
}//end LoadFollowingInst