package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.Curve;

/**
 * Relationship between the unit's emission rate in units of mass per hour (Y-
 * axis) and output active power (X-axis) for a given type of emission. This curve
 * applies when only one type of fuel is being burned.
 * @created 02-Jan-2024 10:53:01 PM
 */
public class EmissionCurve extends Curve {

	/**
	 * The emission content per quantity of fuel burned.
	 */
	public Emission emissionContent;
	/**
	 * The type of emission, which also gives the production rate measurement unit.
	 * The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the
	 * emissionType is the type of emission (e.g. sulfer dioxide).
	 */
	public EmissionType emissionType;
	/**
	 * Flag is set to true when output is expressed in net active power.
	 */
	public Boolean isNetGrossP;

	public EmissionCurve(){

	}
}//end EmissionCurve