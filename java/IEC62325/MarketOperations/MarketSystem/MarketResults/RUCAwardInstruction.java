package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.MarketProductType;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;

/**
 * This class models the information about the RUC awards.
 * @created 28-Dec-2023 8:25:11 PM
 */
public class RUCAwardInstruction {

	/**
	 * Marginal Price ($/MW) for the commodity (Regulation Up, Regulation Down,
	 * Spinning Reserve, or Non-spinning reserve) for pricing run.
	 */
	public Float clearedPrice;
	/**
	 * major product type may include the following but not limited to:
	 * 
	 * Energy
	 * Regulation Up
	 * Regulation Dn
	 * Spinning Reserve
	 * Non-Spinning Reserve
	 * Operating Reserve
	 */
	public MarketProductType marketProductType;
	/**
	 * The RUC Award of a resource is the portion of the RUC Capacity that is not
	 * under RA or RMR contracts. The RUC Award of a resource is the portion of the
	 * RUC Capacity that is eligible for RUC Availability payment.
	 */
	public Float RUCAward;
	/**
	 * The RUC Capacity of a resource is the difference between (i) the RUC Schedule
	 * and (ii) the higher of the DA Schedule and the Minimum Load.
	 */
	public Float RUCCapacity;
	/**
	 * The RUC Schedule of a resource is its output level that balances the load
	 * forecast used in RUC. The RUC Schedule in RUC is similar to the DA Schedule in
	 * DAM.
	 */
	public Float RUCSchedule;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;

	public RUCAwardInstruction(){

	}
}//end RUCAwardInstruction