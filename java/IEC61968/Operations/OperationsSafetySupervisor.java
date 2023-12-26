package IEC61968.Operations;

import IEC61968.Common.Operator;

/**
 * Operator with responsibility that the work in high voltage installation is
 * executed in a safe manner and according to safety regulation.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OperationsSafetySupervisor extends Operator {

	/**
	 * All safety documents released to this supervisor.
	 */
	public SafetyDocument ReleasedSafetyDocuments;
	/**
	 * All safety documents issued by this supervisor.
	 */
	public SafetyDocument IssuedSafetyDocuments;

	public OperationsSafetySupervisor(){

	}
}//end OperationsSafetySupervisor