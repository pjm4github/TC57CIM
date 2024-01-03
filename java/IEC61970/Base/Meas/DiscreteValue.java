package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Integer;

/**
 * DiscreteValue represents a discrete MeasurementValue.
 * @created 02-Jan-2024 11:18:52 PM
 */
public class DiscreteValue extends MeasurementValue {

	/**
	 * The value to supervise.
	 */
	public Integer value;
	/**
	 * The Control variable associated with the MeasurementValue.
	 */
	public Command Command;

	public DiscreteValue(){

	}
}//end DiscreteValue