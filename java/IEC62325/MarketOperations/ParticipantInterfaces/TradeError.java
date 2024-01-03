package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Trade error and warning messages associated with the rule engine processing of
 * the submitted trade.
 * @created 28-Dec-2023 5:24:00 PM
 */
public class TradeError extends IdentifiedObject {

	/**
	 * hour wihthin the trade for which the error applies
	 */
	public DateTime endTime;
	/**
	 * error message
	 */
	public String errMessage;
	/**
	 * Priority number for the error message
	 */
	public Integer errPriority;
	/**
	 * Timestamp of logged error/warning message
	 */
	public DateTime logTimeStamp;
	/**
	 * Rule identifier which triggered the error/warning message
	 */
	public Integer ruleID;
	/**
	 * hour wihthin the trade for which the error applies
	 */
	public DateTime startTime;

	public TradeError(){

	}
}//end TradeError