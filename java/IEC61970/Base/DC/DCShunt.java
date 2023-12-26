package IEC61970.Base.DC;

import IEC61970.Base.Domain.Capacitance;
import IEC61970.Base.Domain.Resistance;

/**
 * A shunt device within the DC system, typically used for filtering.  Needed for
 * transient and short circuit studies.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DCShunt extends DCConductingEquipment {

	/**
	 * Capacitance of the DC shunt.
	 */
	public Capacitance capacitance;
	/**
	 * Resistance of the DC device.
	 */
	public Resistance resistance;

	public DCShunt(){

	}
}//end DCShunt