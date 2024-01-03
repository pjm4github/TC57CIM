package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.Curve;

/**
 * Relationship between unit heat rate per active power (Y-axis) and  unit output
 * (X-axis). The heat input is from all fuels.
 * @created 02-Jan-2024 10:54:51 PM
 */
public class HeatRateCurve extends Curve {

	/**
	 * Flag is set to true when output is expressed in net active power.
	 */
	public Boolean isNetGrossP;

	public HeatRateCurve(){

	}
}//end HeatRateCurve