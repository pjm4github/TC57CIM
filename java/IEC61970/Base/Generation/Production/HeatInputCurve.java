package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.Curve;

/**
 * Relationship between unit heat input in energy per time for main fuel (Y1-axis)
 * and supplemental fuel (Y2-axis) versus unit output in active power (X-axis).
 * The quantity of main fuel used to sustain generation at this output level is
 * prorated for throttling between definition points. The quantity of supplemental
 * fuel used at this output level is fixed and not prorated.
 * @created 02-Jan-2024 10:54:29 PM
 */
public class HeatInputCurve extends Curve {

	/**
	 * Power output - auxiliary power multiplier adjustment factor.
	 */
	public PU auxPowerMult;
	/**
	 * Power output - auxiliary power offset adjustment factor.
	 */
	public ActivePower auxPowerOffset;
	/**
	 * Heat input - efficiency multiplier adjustment factor.
	 */
	public PU heatInputEff;
	/**
	 * Heat input - offset adjustment factor.
	 */
	public HeatRate heatInputOffset;
	/**
	 * Flag is set to true when output is expressed in net active power.
	 */
	public Boolean isNetGrossP;

	public HeatInputCurve(){

	}
}//end HeatInputCurve