package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A protective action for supporting the integrity of the power system.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:33:16 PM
 */
public class ProtectiveAction extends IdentifiedObject {

	/**
	 * The status of the class set by operation or by signal. Optional field that will
	 * override other status fields.
	 */
	public Boolean enabled;
	/**
	 * The default/normal value used when other active signal/values are missing.
	 */
	public Boolean normalEnabled;
	public Gate GateComCondition;
	public Gate GateEnabledCondition;

	public ProtectiveAction(){

	}
}//end ProtectiveAction