package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Seconds;
import IEC61968.Common.Status;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Signifies an event to trigger one or more activities, such as reading a meter,
 * recalculating a bill, requesting work, when generating units shall be scheduled
 * for maintenance, when a transformer is scheduled to be refurbished, etc.
 * @created 28-Dec-2023 5:22:33 PM
 */
public class MarketScheduledEvent extends IdentifiedObject {

	/**
	 * Category of scheduled event.
	 */
	public String category;
	/**
	 * Duration of the scheduled event, for example, the time to ramp between values.
	 */
	public Seconds duration;
	public Status status;

	public MarketScheduledEvent(){

	}
}//end MarketScheduledEvent