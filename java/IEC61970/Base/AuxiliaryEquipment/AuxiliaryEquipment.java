package TC57CIM.IEC61970.Base.AuxiliaryEquipment;

import TC57CIM.IEC61970.Base.Core.Equipment;
import TC57CIM.IEC61970.Base.Core.Terminal;

/**
 * AuxiliaryEquipment describe equipment that is not performing any primary
 * functions but support for the equipment performing the primary function.
 * AuxiliaryEquipment is attached to primary eqipment via an association with
 * Terminal.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class AuxiliaryEquipment extends Equipment {

	/**
	 * The Terminal at the equipment where the AuxiliaryEquipment is attached.
	 */
	public Terminal Terminal;

	public AuxiliaryEquipment(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}