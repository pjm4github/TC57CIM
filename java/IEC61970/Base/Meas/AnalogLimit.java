package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Float;

/**
 * Limit values for Analog measurements.
 * @created 06-Jan-2024 11:46:51 PM
 */
public class AnalogLimit extends Limit {

	/**
	 * The value to supervise against.
	 */
	public Float value;

	public AnalogLimit(){

	}
}//end AnalogLimit