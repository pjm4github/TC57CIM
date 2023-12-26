package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Common.Crew;
import IEC61968.Common.Operator;

/**
 * Atomic switching action.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchingAction extends IdentifiedObject {

	/**
	 * Free text description of this activity.
	 */
	public String description;
	/**
	 * Actual date and time of this switching step.
	 */
	public DateTime executedDateTime;
	/**
	 * If true, the sequence number serves for presentation purposes only, and the
	 * activity itself may be executed at any time.
	 */
	public Boolean isFreeSequence;
	/**
	 * Date and time when the crew was given the instruction to execute the action;
	 * not applicable if the action is performed by operator remote control.
	 */
	public DateTime issuedDateTime;
	/**
	 * Planned date and time of this switching step.
	 */
	public DateTime plannedDateTime;
	public Crew Crew;
	/**
	 * Operator responsible for this switching step.
	 */
	public Operator Operator;

	public SwitchingAction(){

	}
}//end SwitchingAction