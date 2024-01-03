package IEC61968.Work;

import IEC61970.Base.Domain.PerCent;
import IEC61968.Common.ActivityRecord;

/**
 * Records information about the status of work or work task at a point in time.
 * @created 02-Jan-2024 10:08:09 PM
 */
public class WorkActivityRecord extends ActivityRecord {

	/**
	 * Estimated percentage of completion of this individual work task or overall work
	 * order.
	 */
	public PerCent percentComplete;

	public WorkActivityRecord(){

	}
}//end WorkActivityRecord