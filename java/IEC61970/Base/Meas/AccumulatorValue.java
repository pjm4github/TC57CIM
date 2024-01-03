package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Integer;

/**
 * AccumulatorValue represents an accumulated (counted) MeasurementValue.
 * @created 02-Jan-2024 11:16:53 PM
 */
public class AccumulatorValue extends MeasurementValue {

	/**
	 * The value to supervise. The value is positive.
	 */
	public Integer value;

	public AccumulatorValue(){

	}
}//end AccumulatorValue