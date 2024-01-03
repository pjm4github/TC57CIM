package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.ActivePowerChangeRate;
import IEC61970.Base.Core.Curve;

/**
 * Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus
 * the number of hours (X-axis) the unit was off line.
 * @created 02-Jan-2024 10:58:31 PM
 */
public class StartRampCurve extends Curve {

	/**
	 * The startup ramp rate in gross for a unit that is on hot standby.
	 */
	public ActivePowerChangeRate hotStandbyRamp;

	public StartRampCurve(){

	}
}//end StartRampCurve