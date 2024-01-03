package IEC61968.Common;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Records activity for an entity at a point in time; activity may be for an event
 * that has already occurred or for a planned activity.
 * @created 03-Jan-2024 12:07:40 PM
 */
public class ActivityRecord extends IdentifiedObject {

	/**
	 * Date and time this activity record has been created (different from the 'status.
	 * dateTime', which is the time of a status change of the associated object, if
	 * applicable).
	 */
	public DateTime createdDateTime;
	/**
	 * Reason for event resulting in this activity record, typically supplied when
	 * user initiated.
	 */
	public String reason;
	/**
	 * Severity level of event resulting in this activity record.
	 */
	public String severity;
	/**
	 * Information on consequence of event resulting in this activity record.
	 */
	public Status status;
	/**
	 * Type of event resulting in this activity record.
	 */
	public String type;

	public ActivityRecord(){

	}
}//end ActivityRecord