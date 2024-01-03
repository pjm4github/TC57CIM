package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Float;

/**
 * An analog control that issue a set point value.
 * @created 02-Jan-2024 11:25:13 PM
 */
public class SetPoint extends AnalogControl {

	/**
	 * Normal value for Control.value e.g. used for percentage scaling.
	 */
	public Float normalValue;
	/**
	 * The value representing the actuator output.
	 */
	public Float value;

	public SetPoint(){

	}
}//end SetPoint