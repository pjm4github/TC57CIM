package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A conditions that can trigger remedial actions.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:35:20 PM
 */
public class TriggerCondition extends IdentifiedObject {

	public RemedialActionScheme RemedialActionScheme;
	public Gate GateTrigger;

	public TriggerCondition(){

	}
}//end TriggerCondition