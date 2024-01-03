package IEC61970.Base.Generation.Production;

import IEC61970.Base.Core.Curve;

/**
 * The quantity of main fuel (Y-axis) used to restart and repay the auxiliary
 * power consumed versus the number of hours (X-axis) the unit was off line.
 * @created 02-Jan-2024 10:58:13 PM
 */
public class StartMainFuelCurve extends Curve {

	/**
	 * Type of main fuel.
	 */
	public FuelType mainFuelType;

	public StartMainFuelCurve(){

	}
}//end StartMainFuelCurve