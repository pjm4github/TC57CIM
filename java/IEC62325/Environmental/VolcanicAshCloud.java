package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.ParticulateDensity;
import IEC61970.Base.Domain.Length;

/**
 * An ash cloud formed as a result of a volcanic eruption.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class VolcanicAshCloud extends AtmosphericPhenomenon {

	/**
	 * Particulate density of the ash cloud during the time interval.
	 */
	public ParticulateDensity density;
	/**
	 * The diameter of the particles during the time interval.
	 */
	public Length particleSize;

	public VolcanicAshCloud(){

	}
}//end VolcanicAshCloud