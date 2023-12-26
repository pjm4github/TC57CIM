package IEC61970.Base.OperationalLimits;

import IEC61970.Base.Domain.ApparentPower;

/**
 * Apparent power limit.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class ApparentPowerLimit extends OperationalLimit {

	/**
	 * The normal apparent power limit.
	 */
	public ApparentPower normalValue;
	/**
	 * The apparent power limit.
	 */
	public ApparentPower value;

	public ApparentPowerLimit(){

	}
}//end ApparentPowerLimit