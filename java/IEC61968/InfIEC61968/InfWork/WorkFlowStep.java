package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Integer;
import IEC61968.Common.Status;
import IEC61968.Work.Work;

/**
 * A pre-defined set of work steps for a given type of work.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class WorkFlowStep extends WorkIdentifiedObject {

	/**
	 * Used to define dependencies of each work flow step, which is for the instance
	 * of WorkTask associated with a given instance of WorkFlow.
	 */
	public Integer sequenceNumber;
	public Status status;
	public OldWorkTask WorkTasks;
	public Work Work;

	public WorkFlowStep(){

	}
}//end WorkFlowStep