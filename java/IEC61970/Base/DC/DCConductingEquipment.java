package IEC61970.Base.DC;

import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Core.Equipment;

/**
 * The parts of the DC power system that are designed to carry current or that are
 * conductively connected through DC terminals.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DCConductingEquipment extends Equipment {

	/**
	 * Rated DC device voltage. Converter configuration data used in power flow.
	 */
	public Voltage ratedUdc;
	/**
	 * A DC conducting equipment has DC terminals.
	 */
	public DCTerminal DCTerminals;

	public DCConductingEquipment(){

	}
}//end DCConductingEquipment