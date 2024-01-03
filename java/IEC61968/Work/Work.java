package IEC61968.Work;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61968.InfIEC61968.InfWork.Project;

/**
 * Document used to request, initiate, track and record work.
 * @created 02-Jan-2024 10:07:51 PM
 */
public class Work extends BaseWork {

	/**
	 * Date and time work was requested.
	 */
	public DateTime requestDateTime;
	/**
	 * Work order number (or other unique identifying information) for this work.
	 */
	public String workOrderNumber;
	public Project Project;
	/**
	 * All tasks in this work.
	 */
	public WorkTask WorkTasks;
	public ErpProjectAccounting ErpProjectAccounting;

	public Work(){

	}
}//end Work