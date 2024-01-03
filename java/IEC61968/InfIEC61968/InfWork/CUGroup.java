package IEC61968.InfIEC61968.InfWork;

import IEC61968.Common.Status;

/**
 * A Compatible Unit Group identifies a set of compatible units which may be
 * jointly utilized for estimating and designating jobs.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CUGroup extends WorkIdentifiedObject {

	public Status status;
	public CUGroup ChildCUGroups;

	public CUGroup(){

	}
}//end CUGroup