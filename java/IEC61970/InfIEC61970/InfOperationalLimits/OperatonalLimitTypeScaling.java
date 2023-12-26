package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.OperationalLimits.OperationalLimitType;

/**
 * One operational limit type scales values of another operational limit type when
 * under the same operational limit set.    This applies to any operational limit
 * assigned to the target operational limit type and without other limit
 * dependency models.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OperatonalLimitTypeScaling {

	/**
	 * The percentage scaling of the source limit to compute the target limit.  Applys
	 * to operational limits within an operaitonal limit set when both source and
	 * target operational limit types exist.
	 */
	public PerCent scalingPercent;
	public OperationalLimitType SourceOperationalLimitType;
	public OperationalLimitType TargetOperationalLimit;

	public OperatonalLimitTypeScaling(){

	}
}//end OperatonalLimitTypeScaling