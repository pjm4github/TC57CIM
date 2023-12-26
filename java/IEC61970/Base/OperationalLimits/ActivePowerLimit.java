package IEC61970.Base.OperationalLimits;

import IEC61970.Base.Domain.ActivePower;

/**
 * Limit on active power flow.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class ActivePowerLimit extends OperationalLimit {

	/**
	 * The normal value of active power limit.
	 */
	public ActivePower normalValue;
	/**
	 * Value of active power limit.
	 */
	public ActivePower value;

	public ActivePowerLimit(){

	}
}//end ActivePowerLimit