package IEC61970.Base.Meas;

import IEC61970.Base.Domain.String;

/**
 * StringMeasurementValue represents a measurement value of type string.
 * @created 02-Jan-2024 11:26:00 PM
 */
public class StringMeasurementValue extends MeasurementValue {

	/**
	 * The value to supervise.
	 */
	public String value;
	/**
	 * Measurement to which this value is connected.
	 */
	public StringMeasurement StringMeasurement;

	public StringMeasurementValue(){

	}
}//end StringMeasurementValue