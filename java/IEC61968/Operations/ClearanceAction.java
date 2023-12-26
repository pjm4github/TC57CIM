package IEC61968.Operations;


/**
 * Action on clearance document as a switching step.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class ClearanceAction extends SwitchingAction {

	/**
	 * Clearance action to perform.
	 */
	public ClearanceActionKind kind;
	/**
	 * Clearance associated with this clearance action.
	 */
	public ClearanceDocument Clearance;

	public ClearanceAction(){

	}
}//end ClearanceAction