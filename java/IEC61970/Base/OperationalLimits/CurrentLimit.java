package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Domain.CurrentFlow;

/**
 * Operational limit on current.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class CurrentLimit extends OperationalLimit {

	/**
	 * The normal value for limit on current flow.
	 */
	public CurrentFlow normalValue;
	/**
	 * Limit on current flow.
	 */
	public CurrentFlow value;

	public CurrentLimit(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}