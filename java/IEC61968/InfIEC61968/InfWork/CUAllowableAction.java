package IEC61968.InfIEC61968.InfWork;

import IEC61968.Common.Status;

/**
 * Allowed actions: Install, Remove, Transfer, Abandon, etc.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CUAllowableAction extends WorkIdentifiedObject {

	public Status status;
	public CompatibleUnit CompatibleUnits;

	public CUAllowableAction(){

	}
}//end CUAllowableAction