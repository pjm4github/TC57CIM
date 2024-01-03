package IEC61968.Work;

import IEC61968.Common.Priority;
import IEC61968.Common.Document;

/**
 * Common representation for work and work tasks.
 * @author T. Kostic
 * @version 1.0
 * @created 02-Jan-2024 10:04:20 PM
 */
public class BaseWork extends Document {

	/**
	 * Kind of work.
	 */
	public WorkKind kind;
	/**
	 * Priority of work.
	 */
	public Priority priority;
	/**
	 * Kind of work status.
	 */
	public WorkStatusKind statusKind;
	/**
	 * All activity records for this work or work task.
	 */
	public WorkActivityRecord WorkActivityRecords;
	/**
	 * Location for this work/task.
	 */
	public WorkLocation WorkLocation;
	/**
	 * All time schedules for this work or work task.
	 */
	public WorkTimeSchedule TimeSchedules;

	public BaseWork(){

	}
}//end BaseWork