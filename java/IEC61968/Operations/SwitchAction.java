package IEC61968.Operations;

import IEC61970.Base.Wires.Switch;

/**
 * Action on switch as a switching step.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchAction extends SwitchingAction {

	/**
	 * Switching action to perform.
	 */
	public SwitchActionKind kind;
	/**
	 * Switch that is the object of this switch action.
	 */
	public Switch OperatedSwitch;

	public SwitchAction(){

	}
}//end SwitchAction