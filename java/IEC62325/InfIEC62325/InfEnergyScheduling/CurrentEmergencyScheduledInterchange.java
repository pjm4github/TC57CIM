package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Control area emergency schedules
 * @created 03-Jan-2024 1:49:41 PM
 */
public class CurrentEmergencyScheduledInterchange extends IdentifiedObject {

	/**
	 * Net tie MW. These are three entries, the current emergency schedule interchange
	 * and the two future schedules if they exist.
	 */
	public Float emergencyScheduleMW;
	/**
	 * Ramp time, the ramping time for a schedule. This is calculated as the remaining
	 * time to ramp if a schedule is ramping. Measured in seconds, but can be
	 * negattive.
	 */
	public Integer emergencyScheduleRampTime;
	/**
	 * Net tie time,  the start time for a schedule. This is calculated as the current
	 * time if a schedule is ramping.
	 */
	public DateTime emergencyScheduleStartTime;
	public InternalControlArea InternalControlArea;

	public CurrentEmergencyScheduledInterchange(){

	}
}//end CurrentEmergencyScheduledInterchange