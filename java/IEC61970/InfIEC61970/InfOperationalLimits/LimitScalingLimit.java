package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.OperationalLimits.OperationalLimit;

/**
 * Specifies an operational  limit is calculated by scaling another operational
 * limit.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class LimitScalingLimit extends LimitDependency {

	/**
	 * The associated source limit is scaled by this value to compute the limit of the
	 * dependency model.
	 */
	public PerCent limitScalingPercent;
	public OperationalLimit SourceOperationalLimit;

	public LimitScalingLimit(){

	}
}//end LimitScalingLimit