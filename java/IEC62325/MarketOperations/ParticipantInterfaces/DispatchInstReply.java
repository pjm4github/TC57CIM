package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.ActivePower;
import IEC62325.MarketOperations.MktDomain.DispatchResponseType;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.PassIndicatorType;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Response from registered resource acknowledging receipt of dispatch
 * instructions.
 * @created 28-Dec-2023 5:20:50 PM
 */
public class DispatchInstReply extends IdentifiedObject {

	/**
	 * The accepted mw amount by the responder. aka response mw.
	 */
	public ActivePower acceptMW;
	/**
	 * The accept status submitted by the responder. enumeration type needs to be
	 * defined
	 */
	public DispatchResponseType acceptStatus;
	/**
	 * The Subject DN is the X509 Certificate Subject DN. This is the essentially the
	 * certificate name presented by the client. In the case of ADS Certificates, this
	 * will be the user name. It may be from an API Client or the MP Client (GUI).
	 * 
	 * The Subject ID normally includes more than just the user name (Common Name), it
	 * can also contain information such as City, Company ID, etc.
	 */
	public String certificationName;
	/**
	 * MW amount associated with instruction.  For 5 minute binding dispatches, this
	 * is the Goto MW or DOT
	 */
	public ActivePower clearedMW;
	/**
	 * The target date/time for the received instruction.
	 */
	public DateTime instructionTime;
	/**
	 * instruction type:
	 * 
	 * commitment
	 * out of sequence
	 * dispatch
	 */
	public String instructionType;
	/**
	 * The type of run for the market clearing.
	 */
	public PassIndicatorType passIndicator;
	/**
	 * Timestamp indicating the time at which the instruction was received.  
	 */
	public DateTime receivedTime;
	/**
	 * start time
	 */
	public DateTime startTime;

	public DispatchInstReply(){

	}
}//end DispatchInstReply