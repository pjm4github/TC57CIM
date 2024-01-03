package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Float;

/**
 * AnalogValue represents an analog MeasurementValue.
 * @created 02-Jan-2024 11:15:47 PM
 */
public class AnalogValue extends MeasurementValue {

	/**
	 * The value to supervise.
	 */
	public Float value;
	/**
	 * The Control variable associated with the MeasurementValue.
	 */
	public AnalogControl AnalogControl;

	public AnalogValue(){

	}
}//end AnalogValue