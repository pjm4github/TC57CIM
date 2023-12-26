package IEC61970.Base.OperationalLimits;

import IEC61970.Base.Domain.CurrentFlow;

/**
 * Operational limit on current.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
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
}//end CurrentLimit