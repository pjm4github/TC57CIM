package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC62325.MarketOperations.MktDomain.ActionType;

/**
 * Action request against an existing Trade.
 * @created 28-Dec-2023 5:17:29 PM
 */
public class ActionRequest {

	/**
	 * Action name type for the action request.
	 */
	public ActionType actionName;
	public Bid Bid;
	public Trade Trade;

	public ActionRequest(){

	}
}//end ActionRequest