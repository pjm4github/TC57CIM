package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Core.IdentifiedObject;
import TC57CIM.IEC61970.InfIEC61970.InfOperationalLimits.LimitDependency;

/**
 * A value associated with a specific kind of limit.
 * The sub class value attribute shall be positive.
 * The sub class value attribute is inversely proportional to OperationalLimitType.
 * acceptableDuration (acceptableDuration for short). A pair of value_x and
 * acceptableDuration_x are related to each other as follows:
 * if value_1 > value_2 > value_3 >... then
 * acceptableDuration_1 < acceptableDuration_2 < acceptableDuration_3 < ...
 * A value_x with direction="high" shall be greater than a value_y with
 * direction="low".
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class OperationalLimit extends IdentifiedObject {

	/**
	 * The limit type associated with this limit.
	 */
	public OperationalLimitType OperationalLimitType;
	/**
	 * The limit dependency models which are used to calculate this limit.   If no
	 * limit dependencies are specified then the native limit value is used.
	 */
	public LimitDependency LimitDependencyModel;

	public OperationalLimit(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}