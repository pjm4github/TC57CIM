package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.Curve;

/**
 * Relationship between unit operating cost (Y-axis) and unit output active power
 * (X-axis). The operating cost curve for thermal units is derived from heat input
 * and fuel costs. The operating cost curve for hydro units is derived from water
 * flow rates and equivalent water costs.
 * @created 02-Jan-2024 10:53:39 PM
 */
public class GenUnitOpCostCurve extends Curve {

	/**
	 * Flag is set to true when output is expressed in net active power.
	 */
	public Boolean isNetGrossP;

	public GenUnitOpCostCurve(){

	}
}//end GenUnitOpCostCurve