package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;

/**
 * A logical step, grouping atomic switching steps that are important to
 * distinguish when they may change topology (e.g. placing a jumper between two
 * cuts).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchingStepGroup {

	/**
	 * Descriptive information concerning the switching step group.
	 */
	public String description;
	/**
	 * If true, the sequence number serves for presentation purposes only, and the
	 * activity itself may be executed at any time.
	 */
	public Boolean isFreeSequence;
	/**
	 * Describes the overall purpose of the steps in this switching step group.
	 */
	public String purpose;
	/**
	 * Order of this activity in the sequence of activities within the switching plan.
	 */
	public Integer sequenceNumber;

	public SwitchingStepGroup(){

	}
}//end SwitchingStepGroup