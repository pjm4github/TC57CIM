package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MktDomain.AutomaticDispatchMode;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Model of market clearing, related to Dispatch Operating Target (model of
 * anticipatory dispatch). Identifies interval.
 * @created 28-Dec-2023 8:21:55 PM
 */
public class InstructionClearingDOT extends MarketFactors {

	/**
	 * Indication that the system is currently operating in a contingency mode.
	 */
	public YesNo contingencyActive;
	public AutomaticDispatchMode dispatchMode;
	public DotInstruction DotInstruction;

	public InstructionClearingDOT(){

	}
}//end InstructionClearingDOT