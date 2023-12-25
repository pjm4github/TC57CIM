package TC57CIM.IEC61970.Base.Meas;


/**
 * This command reset the counter value to zero.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class AccumulatorReset extends Control {

	/**
	 * The accumulator value that is reset by the command.
	 */
	public AccumulatorValue AccumulatorValue;

	public AccumulatorReset(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}