package IEC61970.Base.Protection;

import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * A device that checks current flow values in any direction or designated
 * direction.
 * @created 25-Dec-2023 8:31:55 PM
 */
public class CurrentRelay extends ProtectionEquipment {

	/**
	 * Current limit number one 1 for inverse time pickup.
	 */
	public CurrentFlow currentLimit1;
	/**
	 * Current limit number 2 for inverse time pickup.
	 */
	public CurrentFlow currentLimit2;
	/**
	 * Current limit number 3 for inverse time pickup.
	 */
	public CurrentFlow currentLimit3;
	/**
	 * Set true if the current relay has inverse time characteristic.
	 */
	public Boolean inverseTimeFlag;
	/**
	 * Inverse time delay number 1 for current limit number 1.
	 */
	public Seconds timeDelay1;
	/**
	 * Inverse time delay number 2 for current limit number 2.
	 */
	public Seconds timeDelay2;
	/**
	 * Inverse time delay number 3 for current limit number 3.
	 */
	public Seconds timeDelay3;

	public CurrentRelay(){

	}
}//end CurrentRelay