package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Domain.CurrentFlow;

/**
 * A current limit that is scheduled.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class ScheduledCurrentLimitValue extends ScheduledLimitValue {

	/**
	 * The current flow limit value applicable at the scheduled time.
	 */
	public CurrentFlow value;

	public ScheduledCurrentLimitValue(){

	}
}//end ScheduledCurrentLimitValue