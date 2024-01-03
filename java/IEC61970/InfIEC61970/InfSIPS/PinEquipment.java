package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Core.Equipment;

/**
 * Value associated with Equipment is used as compare.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:32:18 PM
 */
public class PinEquipment extends GateInputPin {

	/**
	 * The compare operation done on the equipment.
	 */
	public PinEquipmentKind kind;
	public Equipment Equipment;

	public PinEquipment(){

	}
}//end PinEquipment