package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Domain.Voltage;

/**
 * Operational limit applied to voltage.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:30 PM
 */
public class VoltageLimit extends OperationalLimit {

	/**
	 * The normal limit on voltage. High or low limit nature of the limit depends upon
	 * the properties of the operational limit type.
	 */
	public Voltage normalValue;
	/**
	 * Limit on voltage. High or low limit nature of the limit depends upon the
	 * properties of the operational limit type.
	 */
	public Voltage value;

	public VoltageLimit(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}