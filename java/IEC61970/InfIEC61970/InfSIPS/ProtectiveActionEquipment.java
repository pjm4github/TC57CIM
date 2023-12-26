package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.Equipment;

/**
 * Protective action to put an Equipment in-service/out-of-service.
 * @author sveinols
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class ProtectiveActionEquipment extends ProtectiveAction {

	/**
	 * If true the equipment is put in-service, otherwise out-of-service.
	 */
	public Boolean inService;
	public Equipment Equipment;

	public ProtectiveActionEquipment(){

	}
}//end ProtectiveActionEquipment