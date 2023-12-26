package IEC61968.Assets;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Date;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Up-to-date, of-record summary of switch operation information, distilled from a
 * variety of sources (real-time data or real-time data historian, field
 * inspections, etc.) of use to asset health analytics.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchOperationSummary extends IdentifiedObject {

	/**
	 * Total breaker fault operations to date.
	 */
	public Integer lifetimeFaultOperations;
	/**
	 * Total motor starts to date.
	 */
	public Integer lifetimeMotorStarts;
	/**
	 * Total breaker operations to date (including fault and non-fault).
	 */
	public Integer lifetimeTotalOperations;
	/**
	 * Date of most recent breaker fault operation.
	 */
	public Date mostRecentFaultOperationDate;
	/**
	 * Date of most recent motor start.
	 */
	public Date mostRecentMotorStartDate;
	/**
	 * Date of most recent breaker operation (fault or non-fault).
	 */
	public Date mostRecentOperationDate;
	/**
	 * Breaker asset to which this operation information applies.
	 */
	public Asset Breaker;

	public SwitchOperationSummary(){

	}
}//end SwitchOperationSummary