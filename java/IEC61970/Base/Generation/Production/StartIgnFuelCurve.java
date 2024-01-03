package IEC61970.Base.Generation.Production;

import IEC61970.Base.Core.Curve;

/**
 * The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary
 * power consumed versus the number of hours (X-axis) the unit was off line.
 * @created 02-Jan-2024 10:57:59 PM
 */
public class StartIgnFuelCurve extends Curve {

	/**
	 * Type of ignition fuel.
	 */
	public FuelType ignitionFuelType;

	public StartIgnFuelCurve(){

	}
}//end StartIgnFuelCurve