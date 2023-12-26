package IEC62325.MarketManagement;

import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.Time;

/**
 * The date and/or the time.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class DateAndOrTime {

	/**
	 * Date as "yyyy-mm-dd", which conforms with ISO 8601
	 */
	public Date date;
	/**
	 * Time as "hh:mm:ss.sssZ", which conforms with ISO 8601.
	 */
	public Time time;
	public MarketDocument MarketDocument;

	public DateAndOrTime(){

	}
}//end DateAndOrTime