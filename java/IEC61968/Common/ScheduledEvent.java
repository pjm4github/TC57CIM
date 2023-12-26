package IEC61968.Common;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.String;
import IEC61968.Assets.Asset;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An event to trigger one or more activities, such as reading a meter,
 * recalculating a bill, requesting work, when generating units must be scheduled
 * for maintenance, when a transformer is scheduled to be refurbished, etc.
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ScheduledEvent extends IdentifiedObject {

	/**
	 * Duration of the scheduled event, for example, the time to ramp between values.
	 */
	public Seconds duration;
	public Status status;
	/**
	 * Type of scheduled event.
	 */
	public String type;
	public Asset Assets;

	public ScheduledEvent(){

	}
}//end ScheduledEvent