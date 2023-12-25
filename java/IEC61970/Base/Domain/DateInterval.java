package TC57CIM.IEC61970.Base.Domain;


/**
 * Interval between two dates.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class DateInterval {

	/**
	 * End date of this interval.
	 */
	public Date end;
	/**
	 * Start date of this interval.
	 */
	public Date start;

	public DateInterval(){

	}

	public void finalize() throws Throwable {

	}

}