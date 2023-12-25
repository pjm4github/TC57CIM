package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Domain.Voltage;
import TC57CIM.IEC61970.Base.Core.Equipment;

/**
 * The parts of the DC power system that are designed to carry current or that are
 * conductively connected through DC terminals.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}