package TC57CIM.IEC61970.Base.Domain;


/**
 * Interval between two date and time points.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class DateTimeInterval {

	/**
	 * End date and time of this interval.
	 */
	public DateTime end;
	/**
	 * Start date and time of this interval.
	 */
	public DateTime start;

	public DateTimeInterval(){

	}

	public void finalize() throws Throwable {

	}

}