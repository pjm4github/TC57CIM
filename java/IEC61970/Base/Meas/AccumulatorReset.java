package IEC61970.Base.Meas;


/**
 * This command reset the counter value to zero.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:53 PM
 */
public class AccumulatorReset extends Control {

	/**
	 * The accumulator value that is reset by the command.
	 */
	public AccumulatorValue AccumulatorValue;

	public AccumulatorReset(){

	}
}//end AccumulatorReset