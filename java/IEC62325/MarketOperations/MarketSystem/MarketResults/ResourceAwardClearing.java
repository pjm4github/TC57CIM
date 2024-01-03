package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MktDomain.AutomaticDispatchMode;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Models details of bid and offer market clearing. Class indicates whether a
 * contingency is active and whether the automatic dispatching system is active
 * for this interval of the market solution.
 * @created 28-Dec-2023 8:25:21 PM
 */
public class ResourceAwardClearing extends MarketFactors {

	/**
	 * Indication that the system is currently operating in a contingency mode.
	 */
	public YesNo contingencyActive;
	public AutomaticDispatchMode dispatchMode;
	public RUCAwardInstruction RUCAwardInstruction;
	public ResourceAwardInstruction ResourceAwardInstruction;

	public ResourceAwardClearing(){

	}
}//end ResourceAwardClearing