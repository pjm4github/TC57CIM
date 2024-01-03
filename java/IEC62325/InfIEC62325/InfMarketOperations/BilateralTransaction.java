package IEC62325.InfIEC62325.InfMarketOperations;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;

/**
 * Bilateral transaction
 * @created 03-Jan-2024 1:53:43 PM
 */
public class BilateralTransaction {

	/**
	 * Maximum curtailment time in number of trading intervals
	 */
	public Integer curtailTimeMax;
	/**
	 * Minimum curtailment time in number of trading intervals
	 */
	public Integer curtailTimeMin;
	/**
	 * Market type (default=DA)
	 * DA - Day Ahead
	 * RT - Real Time
	 * HA - Hour Ahead
	 */
	public String marketType;
	/**
	 * Maximum purchase time in number of trading intervals
	 */
	public Integer purchaseTimeMax;
	/**
	 * Minimum purchase time in number of trading intervals
	 */
	public Integer purchaseTimeMin;
	/**
	 * Transaction scope:
	 * 'Internal' (default)
	 * 'External'
	 */
	public String scope;
	/**
	 * Maximum total transmission (congestion) charges in monetary units
	 */
	public Money totalTranChargeMax;
	/**
	 * Transaction type (default 1)
	 * 1 - Fixed
	 * 2 - Dispatchable continuous
	 * 3 - Dispatchable block-loading
	 */
	public String transactionType;

	public BilateralTransaction(){

	}
}//end BilateralTransaction