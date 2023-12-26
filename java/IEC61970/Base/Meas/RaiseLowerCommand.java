package IEC61970.Base.Meas;


/**
 * An analog control that increase or decrease a set point value with pulses.
 * Unless otherwise specified, one pulse moves the set point by one.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class RaiseLowerCommand extends AnalogControl {

	/**
	 * The ValueAliasSet used for translation of a Control value to a name.
	 */
	public ValueAliasSet ValueAliasSet;

	public RaiseLowerCommand(){

	}
}//end RaiseLowerCommand