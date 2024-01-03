package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Integer;

/**
 * A Command is a discrete control used for supervisory control.
 * @created 02-Jan-2024 11:16:01 PM
 */
public class Command extends Control {

	/**
	 * Normal value for Control.value e.g. used for percentage scaling.
	 */
	public Integer normalValue;
	/**
	 * The value representing the actuator output.
	 */
	public Integer value;
	/**
	 * The ValueAliasSet used for translation of a Control value to a name.
	 */
	public ValueAliasSet ValueAliasSet;

	public Command(){

	}
}//end Command