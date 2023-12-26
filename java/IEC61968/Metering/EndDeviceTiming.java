package IEC61968.Metering;

import IEC61970.Base.Domain.Minutes;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTimeInterval;

/**
 * Timing for the control actions of end devices.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceTiming {

	/**
	 * Duration of the end device control action or the business event that is the
	 * subject of the end device control.
	 */
	public Minutes duration;
	/**
	 * True if 'duration' is indefinite.
	 */
	public Boolean durationIndefinite;
	/**
	 * Start and end time of an interval during which end device control actions are
	 * to be executed.
	 */
	public DateTimeInterval interval;
	/**
	 * Kind of randomisation to be applied to the end device control actions to be
	 * executed.
	 */
	public RandomisationKind randomisation;

	public EndDeviceTiming(){

	}
}//end EndDeviceTiming