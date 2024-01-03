package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.DispatchResponseType;
import IEC62325.MarketOperations.MktDomain.PassIndicatorType;
import IEC61970.Base.Domain.DateTime;

/**
 * Response from an intertie resource acknowledging receipt of dispatch
 * instructions.
 * @created 28-Dec-2023 5:21:39 PM
 */
public class InterTieDispatchResponse {

	/**
	 * The accepted mw amount by the responder. aka response mw. 
	 */
	public Float acceptMW;
	/**
	 * The accept status submitted by the responder. Valid values are NON-RESPONSE,
	 * ACCEPT, DECLINE, PARTIAL.
	 */
	public DispatchResponseType acceptStatus;
	/**
	 * MW amount associated with instruction.  For 5 minute binding dispatches, this
	 * is the Goto MW or DOT
	 */
	public Float clearedMW;
	/**
	 * Part of the Composite key that downstream app uses to match the instruction
	 */
	public PassIndicatorType passIndicator;
	/**
	 * Part of the Composite key that downstream app uses to match the instruction
	 */
	public DateTime startTime;

	public InterTieDispatchResponse(){

	}
}//end InterTieDispatchResponse