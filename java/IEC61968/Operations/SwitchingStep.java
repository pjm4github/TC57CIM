package IEC61968.Operations;

import IEC61970.Base.Domain.Integer;

/**
 * A step in a Switching Step Group.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchingStep {

	/**
	 * the sequence number of the switching step within the switching step group
	 */
	public Integer sequenceNumber;
	public SwitchingStepGroup SwitchingStepGroup;
	public SwitchingAction SwitchingAction;

	public SwitchingStep(){

	}
}//end SwitchingStep