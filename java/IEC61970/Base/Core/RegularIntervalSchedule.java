package IEC61970.Base.Core;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Seconds;

/**
 * The schedule has time points where the time between them is constant.
 * @created 02-Jan-2024 10:37:07 PM
 */
public class RegularIntervalSchedule extends BasicIntervalSchedule {

	/**
	 * The time for the last time point.  The value can be a time of day, not a
	 * specific date.
	 */
	public DateTime endTime;
	/**
	 * The time between each pair of subsequent regular time points in sequence order.
	 */
	public Seconds timeStep;
	/**
	 * The regular interval time point data values that define this schedule.
	 */
	public RegularTimePoint TimePoints;

	public RegularIntervalSchedule(){

	}
}//end RegularIntervalSchedule