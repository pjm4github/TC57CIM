package IEC62325.MarketManagement;

import IEC61970.Base.Domain.Duration;
import IEC61970.Base.Domain.DateTimeInterval;

/**
 * An identification of a time interval that may have a given resolution.
 * @author effantin-cyr
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class Period {

	/**
	 * The number of units of time that compose an individual step within a period.
	 */
	public Duration resolution;
	/**
	 * The start and end date and time for a given interval.
	 */
	public DateTimeInterval timeInterval;
	public Reason Reason;

	public Period(){

	}
}//end Period