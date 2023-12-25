package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Domain.Inductance;
import TC57CIM.IEC61970.Base.Domain.Resistance;

/**
 * A series device within the DC system, typically a reactor used for filtering or
 * smoothing.  Needed for transient and short circuit studies.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class DCSeriesDevice extends DCConductingEquipment {

	/**
	 * Inductance of the device.
	 */
	public Inductance inductance;
	/**
	 * Resistance of the DC device.
	 */
	public Resistance resistance;

	public DCSeriesDevice(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}