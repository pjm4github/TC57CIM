package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * Verification of a switch position or other condition as a switching step
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public class VerificationAction extends SwitchingAction {

	/**
	 * freeform description of the condition to be verified
	 */
	public String verificationCondition;
	public PowerSystemResource PowerSystemResource;

	public VerificationAction(){

	}
}//end VerificationAction