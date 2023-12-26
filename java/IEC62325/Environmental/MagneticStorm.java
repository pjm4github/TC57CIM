package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.MagneticField;

/**
 * A magnetic storm, a temporary disturbance of the earth's magnetic field,
 * induced by radiation and streams of charged particles from the sun.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MagneticStorm extends SpacePhenomenon {

	/**
	 * Change in the disturbance  - storm time (Dst) index. The size of a geomagnetic
	 * storm is classified as:
	 * - moderate ( -50 nT >minimum of Dst > -100 nT)
	 * - intense (-100 nT > minimum Dst > -250 nT) or
	 * - super-storm ( minimum of Dst < -250 nT).
	 */
	public MagneticField changeDst;

	public MagneticStorm(){

	}
}//end MagneticStorm