package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Model of market results, instruction for resource.  Contains details of award
 * as attributes.
 * @created 28-Dec-2023 8:25:31 PM
 */
public class ResourceAwardInstruction {

	/**
	 * For DA Energy: Not Applicable;
	 * 
	 * For DA AS: DA AS market award;
	 * 
	 * For RT Energy: Not Applicable;
	 * 
	 * For RT AS: RT AS market award (excluding DA AS market or self-proviison awards)
	 */
	public Float awardMW;
	/**
	 * For DA Energy: Total Schedule = DA market schedule + DA self-schedule award;
	 * 
	 * 
	 * For DA AS: DA Ancillary Service Awards = DA AS market award + DA AS self-
	 * provision award;
	 * 
	 * For RT Energy: Total Schedule = RT market schedule + RT self-schedule award;
	 * 
	 * 
	 * For RT AS: RT Ancillary Service Awards = RT AS self-provision award + RT AS
	 * market award + DA AS market award + DA AS self-provision award;
	 */
	public Float clearedMW;
	/**
	 * Marginal Price ($/MW) for the commodity (Regulation Up, Regulation Down,
	 * Spinning Reserve, or Non-spinning reserve) for pricing run.
	 */
	public Float clearedPrice;
	/**
	 * Congestion component of Location Marginal Price (LMP) in monetary units per MW.
	 */
	public Float congestLMP;
	/**
	 * Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.
	 */
	public Float costLMP;
	/**
	 * The tier2 mw added by dispatcher action
	 * Market results of the synchronized reserve market
	 */
	public Float dispatcherAddedMW;
	/**
	 * Unit max output for dispatch; bid in economic maximum
	 */
	public Float economicMax;
	/**
	 * Unit min output for dispatch; bid in economic minimum
	 */
	public Float economicMin;
	/**
	 * Effective Regulation Down Limit (MW)
	 */
	public Float effRegulationDownLimit;
	/**
	 * Effective Regulation Up Limit 
	 */
	public Float effRegulationUpLimit;
	/**
	 * Locational marginal price value
	 */
	public Float lmp;
	/**
	 * Loss component of Location Marginal Price (LMP) in monetary units per MW.
	 */
	public Float lossLMP;
	/**
	 * Indicates if an award was manually blocked (Y/N). Valid for Spinning and Non-
	 * spinning.
	 */
	public YesNo manuallyBlocked;
	/**
	 * Indicator (Yes / No) that this resource set the price for this dispatch /
	 * schedule.
	 */
	public YesNo marginalResourceIndicator;
	/**
	 * Identifes if the unit was set to must run by the market participant responsible
	 * for bidding in the unit
	 */
	public Boolean mustRunInd;
	/**
	 * Unit no-load cost in case of energy commodity
	 */
	public Float noLoadCost;
	/**
	 * Optimal Bid cost
	 */
	public Float optimalBidCost;
	/**
	 * Optimal Bid production payment based on LMP
	 */
	public Float optimalBidPay;
	/**
	 * Optimal Bid production margin
	 */
	public Float optimalMargin;
	/**
	 * Time the manual data entry occured.
	 */
	public DateTime overrideTimeStamp;
	/**
	 * Provides the ability for the grid operator to override items, such as spin
	 * capacity requirements, prior to running the algorithm. This value is market
	 * product based (spin, non-spin, reg up, reg down, or RUC).
	 */
	public Float overrideValue;
	/**
	 * For DA Energy: DA total self-schedule award;
	 * For DA AS: DA AS self-provision award;
	 * For RT Energy: RT total self-schedule award;
	 * For RT AS: RT AS self-provision award (excluding DA AS market or self-provision
	 * awards)
	 */
	public Float selfSchedMW;
	/**
	 * Unit start up cost in case of energy commodity
	 */
	public Float startUpCost;
	/**
	 * In or out status of resource
	 */
	public String status;
	/**
	 * Total bid revenue (startup_cost + no_load_cost + bid_pay)
	 */
	public Float totalRevenue;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;
	public SelfScheduleBreakdown SelfScheduleBreakdown;
	public RegisteredResource RegisteredResource;

	public ResourceAwardInstruction(){

	}
}//end ResourceAwardInstruction