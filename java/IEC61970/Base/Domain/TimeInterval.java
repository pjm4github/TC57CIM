package TC57CIM.IEC61970.Base.Domain;


/**
 * Interval between two times.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:30 PM
 */
public class TimeInterval {

	/**
	 * End time of this interval.
	 */
	public Time end;
	/**
	 * Start time of this interval.
	 */
	public Time start;

	public TimeInterval(){

	}

	public void finalize() throws Throwable {

	}

}