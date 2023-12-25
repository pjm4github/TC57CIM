package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Domain.Capacitance;
import TC57CIM.IEC61970.Base.Domain.Resistance;

/**
 * A shunt device within the DC system, typically used for filtering.  Needed for
 * transient and short circuit studies.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}