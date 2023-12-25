package TC57CIM.IEC61970.Base.Domain;


/**
 * Interval between two times specified as mont and date.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class MonthDayInterval {

	/**
	 * End time of this interval.
	 */
	public MonthDay end;
	/**
	 * Start time of this interval.
	 */
	public MonthDay start;

	public MonthDayInterval(){

	}

	public void finalize() throws Throwable {

	}

}