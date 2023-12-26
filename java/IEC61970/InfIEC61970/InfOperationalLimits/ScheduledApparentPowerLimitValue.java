package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Domain.ApparentPower;

/**
 * A time scheduled value for apparent power limit.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class ScheduledApparentPowerLimitValue extends ScheduledLimitValue {

	/**
	 * The apparent power limit value for the scheduled time.
	 */
	public ApparentPower value;

	public ScheduledApparentPowerLimitValue(){

	}
}//end ScheduledApparentPowerLimitValue