package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Domain.ApparentPower;

/**
 * Apparent power limit.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}