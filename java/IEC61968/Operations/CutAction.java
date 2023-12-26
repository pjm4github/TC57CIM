package IEC61968.Operations;

import IEC61970.Base.Wires.Cut;

/**
 * Action on cut as a switching step.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class CutAction extends SwitchingAction {

	/**
	 * Switching action to perform.
	 */
	public TempEquipActionKind kind;
	/**
	 * Cut on which this action is taken.
	 */
	public Cut Cut;

	public CutAction(){

	}
}//end CutAction