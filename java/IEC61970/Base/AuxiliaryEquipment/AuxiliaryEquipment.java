package IEC61970.Base.AuxiliaryEquipment;

import IEC61970.Base.Core.Equipment;
import IEC61970.Base.Core.Terminal;

/**
 * AuxiliaryEquipment describe equipment that is not performing any primary
 * functions but support for the equipment performing the primary function.
 * AuxiliaryEquipment is attached to primary eqipment via an association with
 * Terminal.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AuxiliaryEquipment extends Equipment {

	/**
	 * The Terminal at the equipment where the AuxiliaryEquipment is attached.
	 */
	public Terminal Terminal;

	public AuxiliaryEquipment(){

	}
}//end AuxiliaryEquipment