package IEC61970.Base.LoadModel;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Group of similar days.   For example it could be used to represent weekdays,
 * weekend, or holidays.
 * @created 02-Jan-2024 11:12:01 PM
 */
public class DayType extends IdentifiedObject {

	/**
	 * Schedules that use this DayType.
	 */
	public SeasonDayTypeSchedule SeasonDayTypeSchedules;

	public DayType(){

	}
}//end DayType