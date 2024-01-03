package IEC61970.Base.Core;

import IEC61970.InfIEC61970.InfSIPS.ProtectiveActionAdjustment;

/**
 * The parts of the AC power system that are designed to carry current or that are
 * conductively connected through terminals.
 * @created 02-Jan-2024 10:17:48 PM
 */
public class ConductingEquipment extends Equipment {

	/**
	 * The operating condition to the Conducting Equipment is changed when protective
	 * action adjustment is activated. For Shunt Compensator or other conducting
	 * equipment that operates on discrete values (integer), the values given in float
	 * will be rounded. 
	 */
	public ProtectiveActionAdjustment ProtectiveActionAdjustment;

	public ConductingEquipment(){

	}
}//end ConductingEquipment