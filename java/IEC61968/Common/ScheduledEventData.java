package IEC61968.Common;

import IEC61970.Base.Domain.DateTimeInterval;
import IEC61968.Assets.InspectionDataSet;

/**
 * Schedule parameters for an activity that is to occur, is occurring, or has
 * completed.
 * @created 25-Dec-2023 8:45:24 PM
 */
public class ScheduledEventData {

	/**
	 * Estimated date and time for activity execution (with earliest possibility of
	 * activity initiation and latest possibility of activity completion).
	 */
	public DateTimeInterval estimatedWindow;
	/**
	 * Requested date and time interval for activity execution.
	 */
	public DateTimeInterval requestedWindow;
	public Status status;
	public InspectionDataSet InspectionDataSet;
	/**
	 * All scheduled events with this specification.
	 */
	public ScheduledEvent ScheduledEvents;

	public ScheduledEventData(){

	}
}//end ScheduledEventData