package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Model of results of Market Power tests, and possible mitigation. Interval based.
 * 
 * @created 28-Dec-2023 8:22:37 PM
 */
public class MPMClearing extends MarketFactors {

	public YesNo LMPMFinalFlag;
	public YesNo mitigationOccuredFlag;
	public YesNo SMPMFinalFlag;
	public MPMTestResults MPMTestResults;

	public MPMClearing(){

	}
}//end MPMClearing