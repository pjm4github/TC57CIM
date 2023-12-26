package IEC61970.Base.DC;

import IEC61970.Base.Domain.Inductance;
import IEC61970.Base.Domain.Resistance;

/**
 * A series device within the DC system, typically a reactor used for filtering or
 * smoothing.  Needed for transient and short circuit studies.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
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
}//end DCSeriesDevice