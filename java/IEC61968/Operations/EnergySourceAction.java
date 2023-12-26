package IEC61968.Operations;

import IEC61970.Base.Wires.EnergySource;

/**
 * Action on energy source as a switching step.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EnergySourceAction extends SwitchingAction {

	/**
	 * Switching action to perform.
	 */
	public TempEquipActionKind kind;
	/**
	 * Energy source on which this action is taken.
	 */
	public EnergySource EnergySource;

	public EnergySourceAction(){

	}
}//end EnergySourceAction