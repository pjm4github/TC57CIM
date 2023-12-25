package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Domain.ActivePower;

/**
 * Limit on active power flow.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}