package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.RelativeDisplacement;
import IEC62325.Environmental.EnvDomain.Bearing;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Speed;

/**
 * An atmospheric phenomenon with a base and altitude providing the vertical
 * coverage (combined with the Location to provide three dimensional space).
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class AtmosphericPhenomenon extends EnvironmentalPhenomenon {

	/**
	 * The maximum altitude of the phenomenon.
	 */
	public RelativeDisplacement altitude;
	/**
	 * The base altitude of the phenomenon.
	 */
	public RelativeDisplacement base;
	/**
	 * The direction the phenomenon is moving.
	 */
	public Bearing direction;
	/**
	 * The maximum percentage coverage
	 */
	public PerCent maxCoverage;
	/**
	 * The minimum percentage coverage 
	 */
	public PerCent minCoverage;
	/**
	 * The speed of the phenomenon
	 */
	public Speed speed;

	public AtmosphericPhenomenon(){

	}
}//end AtmosphericPhenomenon