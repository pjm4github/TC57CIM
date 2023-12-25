package TC57CIM.IEC61970.Base.Meas;


/**
 * An analog control that increase or decrease a set point value with pulses.
 * Unless otherwise specified, one pulse moves the set point by one.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:29 PM
 */
public class RaiseLowerCommand extends AnalogControl {

	/**
	 * The ValueAliasSet used for translation of a Control value to a name.
	 */
	public ValueAliasSet ValueAliasSet;

	public RaiseLowerCommand(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}