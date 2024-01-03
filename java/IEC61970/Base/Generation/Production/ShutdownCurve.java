package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.Curve;

/**
 * Relationship between the rate in gross active power/minute (Y-axis) at which a
 * unit should be shutdown and its present gross MW output (X-axis).
 * @created 02-Jan-2024 10:57:43 PM
 */
public class ShutdownCurve extends Curve {

	/**
	 * Fixed shutdown cost.
	 */
	public Money shutdownCost;
	/**
	 * The date and time of the most recent generating unit shutdown.
	 */
	public DateTime shutdownDate;

	public ShutdownCurve(){

	}
}//end ShutdownCurve