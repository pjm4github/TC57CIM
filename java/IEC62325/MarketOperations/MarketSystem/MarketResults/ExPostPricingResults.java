package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;

/**
 * Model of ex-post pricing of nodes.  Includes LMP information, pnode based.
 * @created 28-Dec-2023 8:20:55 PM
 */
public class ExPostPricingResults {

	/**
	 * Congestion component of Location Marginal Price (LMP) in monetary units per MW;
	 * congestion component of the hourly LMP at a specific pricing node
	 * Attribute Usage: Result of the Security, Pricing, and
	 * Dispatch(SPD)/Simultaneous Feasibility Test(SFT) software and denotes the
	 * hourly congestion component of LMP for each pricing node.
	 */
	public Float congestLMP;
	/**
	 * 5 min weighted average LMP; the Location Marginal Price of the Pnode for which
	 * price calculation is carried out.
	 * Attribute Usage: 5 min weighted average LMP  to be displayed on UI
	 */
	public Float lmp;
	/**
	 * Loss component of Location Marginal Price (LMP) in monetary units per MW; loss
	 * component of the hourly LMP at a specific pricing node
	 * Attribute Usage: Result of the Security, Pricing, and
	 * Dispatch(SPD)/Simultaneous Feasibility Test(SFT) software and denotes the
	 * hourly loss component of LMP for each pricing node.
	 */
	public Float lossLMP;
	public ExPostPricing ExPostPricing;

	public ExPostPricingResults(){

	}
}//end ExPostPricingResults