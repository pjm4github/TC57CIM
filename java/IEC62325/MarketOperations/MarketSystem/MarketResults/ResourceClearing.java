package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Model of market results, including cleaing result of resources. Associated with
 * ResourceDispatchResults.
 * @created 28-Dec-2023 8:25:41 PM
 */
public class ResourceClearing extends MarketFactors {

	public ResourceDispatchResults ResourceDispatchResults;
	public ResourceLoadFollowingInst ResourceLoadFollowingInst;

	public ResourceClearing(){

	}
}//end ResourceClearing