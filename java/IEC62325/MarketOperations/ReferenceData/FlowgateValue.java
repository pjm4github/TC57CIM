package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.FlowDirectionType;

/**
 * Day Ahead,  Network Native Load, Economic Dispatch, values used for calculation
 * of Network Native Load (NNL) Determinator process.
 * @created 28-Dec-2023 12:13:45 PM
 */
public class FlowgateValue {

	/**
	 * Limit for Economic Dispatch priority 6 energy flow on the specified flowgate
	 * for the specified time period.
	 */
	public Integer economicDispatchLimit;
	/**
	 * Date/Time when record becomes effective
	 * Used to determine when a record becomes effective
	 */
	public DateTime effectiveDate;
	/**
	 * Limit for firm flow on the specified flowgate for the specified time period.
	 * The amount of energy flow over a specifed flowgate due to generation in the
	 * market which can be classified as Firm Network priority.
	 */
	public Integer firmNetworkLimit;
	/**
	 * Specifies the direction of energy flow in the flowgate
	 */
	public FlowDirectionType flowDirectionFlag;
	/**
	 * The amount of energy flow over a specifed flowgate due to generation in the
	 * market.
	 */
	public Integer mktFlow;
	/**
	 * Net Energy flow in flowgate for the associated FlowgatePartner
	 */
	public Integer netFirmNetworkLimit;

	public FlowgateValue(){

	}
}//end FlowgateValue