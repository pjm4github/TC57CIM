package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.SelfScheduleBreakdownType;

/**
 * Model of Self Schedules Results.  Includes self schedule MW,and type of self
 * schedule for each self schedule type included in total self schedule MW value
 * found in ResourceAwardInstruction.
 * @created 28-Dec-2023 8:26:18 PM
 */
public class SelfScheduleBreakdown {

	/**
	 * Cleared value for the specific self schedule type listed.  
	 */
	public Float selfSchedMW;
	/**
	 * Self schedule breakdown type.
	 */
	public SelfScheduleBreakdownType selfSchedType;

	public SelfScheduleBreakdown(){

	}
}//end SelfScheduleBreakdown