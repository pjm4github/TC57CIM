package IEC61968.Operations;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * Safety document used to authorise work on conducting equipment in the field.
 * Tagged equipment is not allowed to be operated.
 * @created 03-Jan-2024 1:14:52 PM
 */
public class ClearanceDocument extends SafetyDocument {

	/**
	 * If true, the equipment must be deenergised.
	 */
	public Boolean mustBeDeenergised;
	/**
	 * If true, the equipment must be grounded.
	 */
	public Boolean mustBeGrounded;
	/**
	 * All power system resources tagged through this clearance.
	 */
	public PowerSystemResource TaggedPSRs;

	public ClearanceDocument(){

	}
}//end ClearanceDocument