package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Integer;

/**
 * Limit values for Accumulator measurements.
 * @created 03-Jan-2024 4:15:23 PM
 */
public class AccumulatorLimit extends Limit {

	/**
	 * The value to supervise against. The value is positive.
	 */
	public Integer value;

	public AccumulatorLimit(){

	}
}//end AccumulatorLimit