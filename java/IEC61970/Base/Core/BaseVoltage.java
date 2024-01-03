package IEC61970.Base.Core;

import IEC61970.Base.Domain.Voltage;

/**
 * Defines a system base voltage which is referenced.
 * @created 02-Jan-2024 10:16:33 PM
 */
public class BaseVoltage extends IdentifiedObject {

	/**
	 * The power system resource's base voltage.
	 */
	public Voltage nominalVoltage;
	/**
	 * All conducting equipment with this base voltage.  Use only when there is no
	 * voltage level container used and only one base voltage applies.  For example,
	 * not used for transformers.
	 */
	public ConductingEquipment ConductingEquipment;

	public BaseVoltage(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}
}//end BaseVoltage