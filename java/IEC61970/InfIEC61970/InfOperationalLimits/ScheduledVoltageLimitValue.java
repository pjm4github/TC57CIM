package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Domain.Voltage;

/**
 * A voltage limit value for a scheduled time.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class ScheduledVoltageLimitValue extends ScheduledLimitValue {

	/**
	 * The voltage limit value for the scheduled time.
	 */
	public Voltage value;

	public ScheduledVoltageLimitValue(){

	}
}//end ScheduledVoltageLimitValue