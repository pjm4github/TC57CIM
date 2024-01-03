package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Metered Sub-System aggregation of MSS Zones.
 * @created 28-Dec-2023 12:16:37 PM
 */
public class MSSAggregation extends IdentifiedObject {

	/**
	 * Charge for Emission Costs, Start Up Costs, or Minimum Load Costs.
	 */
	public YesNo costRecovery;
	/**
	 * MSS Load Following may select Net vs. Gross settlement.  Net Settlement
	 * requires the net Demand settled at the MSS LAP and Net Supply needs to settle
	 * at the equivalent to the weighted average price of the MSS generation.  Gross
	 * load will be settled at the System LAP and the Gross supply will be settled at
	 * the LMP.  MSS Aggregation that elects gross settlement shall have to identify
	 * if its resources are Load Following or not. 
	 */
	public YesNo grossSettlement;
	/**
	 * Provides an indication if losses are to be ignored for this zone. Also refered
	 * to as Exclude Marginal Losses.
	 */
	public YesNo ignoreLosses;
	/**
	 * Provides an indication if marginal losses are to be ignored for this zone. 
	 */
	public YesNo ignoreMarginalLosses;
	/**
	 * Indication that this particular MSSA participates in the Load Following
	 * function.
	 */
	public YesNo loadFollowing;
	/**
	 * Indicates that RUC will be procured by the ISO or self provided.
	 */
	public YesNo rucProcurement;
	public MeteredSubSystem MeteredSubSystem;
	public RTO RTO;

	public MSSAggregation(){

	}
}//end MSSAggregation