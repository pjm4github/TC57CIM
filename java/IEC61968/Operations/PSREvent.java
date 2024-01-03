package IEC61968.Operations;

import IEC61970.Base.Core.PowerSystemResource;
import IEC61968.Common.ActivityRecord;

/**
 * Event recording the change in operational status of a power system resource;
 * may be for an event that has already occurred or for a planned activity.
 * @created 03-Jan-2024 1:17:09 PM
 */
public class PSREvent extends ActivityRecord {

	/**
	 * Kind of event.
	 */
	public PSREventKind kind;
	/**
	 * Power system resource that generated this event.
	 */
	public PowerSystemResource PowerSystemResource;

	public PSREvent(){

	}
}//end PSREvent