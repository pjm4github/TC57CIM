package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class represent the error information for a bid that is detected during
 * bid validation.
 * @created 28-Dec-2023 5:18:53 PM
 */
public class BidError extends IdentifiedObject {

	public String componentType;
	/**
	 * hour wihthin the bid for which the error applies
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
	public DateTime logTimeStamp;
	public Integer msgLevel;
	public Integer ruleID;
	/**
	 * hour wihthin the bid for which the error applies
	 */
	public DateTime startTime;

	public BidError(){

	}
}//end BidError