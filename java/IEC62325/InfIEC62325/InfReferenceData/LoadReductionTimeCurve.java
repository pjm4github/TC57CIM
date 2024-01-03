package IEC62325.InfIEC62325.InfReferenceData;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.Curve;

/**
 * This is the cureve that describes the load reduction time. Relationship between
 * time (Y1-axis) vs. MW (X-axis).
 * @created 02-Jan-2024 11:55:14 PM
 */
public class LoadReductionTimeCurve extends Curve {

	/**
	 * type of the curve: Possible values are but not limited to:
	 * 
	 * Max, Min,
	 */
	public String loadReductionTimeCurveType;

	public LoadReductionTimeCurve(){

	}
}//end LoadReductionTimeCurve