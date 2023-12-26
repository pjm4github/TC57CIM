package IEC61970.Base.Faults;

import IEC61970.Base.Core.Terminal;

/**
 * A fault applied at the terminal, external to the equipment. This class is not
 * used to specify faults internal to the equipment.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class EquipmentFault extends Fault {

	/**
	 * The terminal connecting to the bus to which the fault is applied.
	 */
	public Terminal Terminal;

	public EquipmentFault(){

	}
}//end EquipmentFault