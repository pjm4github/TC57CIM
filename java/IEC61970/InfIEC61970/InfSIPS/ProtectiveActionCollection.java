package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A collection of protective actions to protect the integrity of the power system.
 * 
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:33:44 PM
 */
public class ProtectiveActionCollection extends IdentifiedObject {

	public StageTrigger StageTrigger;
	public ProtectiveAction ProtectiveAction;

	public ProtectiveActionCollection(){

	}
}//end ProtectiveActionCollection