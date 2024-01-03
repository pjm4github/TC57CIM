package IEC61970.Base.Meas;


/**
 * An AnalogLimitSet specifies a set of Limits that are associated with an Analog
 * measurement.
 * @created 02-Jan-2024 11:15:29 PM
 */
public class AnalogLimitSet extends LimitSet {

	/**
	 * The limit values used for supervision of Measurements.
	 */
	public AnalogLimit Limits;

	public AnalogLimitSet(){

	}
}//end AnalogLimitSet