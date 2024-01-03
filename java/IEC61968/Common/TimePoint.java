package IEC61968.Common;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A point in time within a sequence of points in time relative to a time schedule.
 * 
 * @created 03-Jan-2024 12:13:59 PM
 */
public class TimePoint extends IdentifiedObject {

	/**
	 * Absolute date and time for this time point. For calendar-based time point, it
	 * is typically manually entered, while for interval-based or sequence-based time
	 * point it is derived.
	 */
	public DateTime dateTime;
	/**
	 * (if interval-based) A point in time relative to scheduled start time in
	 * 'TimeSchedule.scheduleInterval.start'.
	 */
	public Seconds relativeTimeInterval;
	/**
	 * (if sequence-based) Relative sequence number for this time point.
	 */
	public Integer sequenceNumber;
	/**
	 * Status of this time point.
	 */
	public Status status;
	/**
	 * Interval defining the window of time that this time point is valid (for example,
	 * seasonal, only on weekends, not on weekends, only 8:00 am to 5:00 pm, etc.).
	 */
	public DateTimeInterval window;

	public TimePoint(){

	}
}//end TimePoint