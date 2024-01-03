package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.Curve;

/**
 * Relationship between unit incremental heat rate in (delta energy/time) per
 * (delta active power) and unit output in active power. The IHR curve represents
 * the slope of the HeatInputCurve. Note that the "incremental heat rate" and the
 * "heat rate" have the same engineering units.
 * @created 02-Jan-2024 10:56:15 PM
 */
public class IncrementalHeatRateCurve extends Curve {

	/**
	 * Flag is set to true when output is expressed in net active power.
	 */
	public Boolean isNetGrossP;

	public IncrementalHeatRateCurve(){

	}
}//end IncrementalHeatRateCurve