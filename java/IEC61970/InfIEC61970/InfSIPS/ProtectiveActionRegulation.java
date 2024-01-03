package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Wires.RegulatingControl;

/**
 * Protective action to change regulation to Equipment.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:34:17 PM
 */
public class ProtectiveActionRegulation extends ProtectiveAction {

	/**
	 * If true the regulator is put in-service, otherwise out-of-service (no
	 * regulation).
	 */
	public Boolean isRegulating;
	/**
	 * The target value specified the new case input for the regulator.  The value has
	 * the units appropriate to the mode attribute. The protective action does not
	 * change the mode attribute.
	 */
	public Float targetValue;
	public RegulatingControl RegulatingControl;

	public ProtectiveActionRegulation(){

	}
}//end ProtectiveActionRegulation