package IEC61970.Base.LoadModel;

import IEC61970.Base.Domain.MonthDay;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A specified time period of the year.
 * @created 02-Jan-2024 11:13:52 PM
 */
public class Season extends IdentifiedObject {

	/**
	 * Date season ends.
	 */
	public MonthDay endDate;
	/**
	 * Date season starts.
	 */
	public MonthDay startDate;
	/**
	 * Schedules that use this Season.
	 */
	public SeasonDayTypeSchedule SeasonDayTypeSchedules;

	public Season(){

	}
}//end Season