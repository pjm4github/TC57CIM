package IEC61970.InfIEC61970.InfAvailabilityPlans;

import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The collection of all the availability schedules for a given time range.  Only
 * one availability plan shall be valid for the same period.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AvailablityPlan extends IdentifiedObject {

	/**
	 * The period of time for which the plan is valid.
	 */
	public DateTimeInterval validPeriod;

	public AvailablityPlan(){

	}
}//end AvailablityPlan