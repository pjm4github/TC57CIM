package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;

/**
 * Control area current net tie (scheduled interchange) sent to real time dispatch.
 * 
 * @created 03-Jan-2024 1:49:41 PM
 */
public class CurrentScheduledInterchange {

	/**
	 * Current control area net tie MW (the sum of the tie line flows, i.e the sum of
	 * flows into and out of the control area), the current instantaneous scheduled
	 * interchange.
	 */
	public Float currentNetTieMW;
	/**
	 * Use Emergency Schedule
	 * Attribute Usage: Emergency use indicator, false = Emergency Schedular OFF, true
	 * = Emergency Schedular ON.
	 */
	public Boolean useEmergencySchedule;
	public InternalControlArea InternalControlArea;

	public CurrentScheduledInterchange(){

	}
}//end CurrentScheduledInterchange