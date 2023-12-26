package IEC61970.Base.OperationalLimits;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The operational meaning of a category of limits.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OperationalLimitType extends IdentifiedObject {

	/**
	 * The nominal acceptable duration of the limit.  Limits are commonly expressed in
	 * terms of the a time limit for which the limit is normally acceptable.   The
	 * actual acceptable duration of a specific limit may depend on other local
	 * factors such as temperature or wind speed.
	 */
	public Seconds acceptableDuration;
	/**
	 * The direction of the limit.
	 */
	public OperationalLimitDirectionKind direction;

	public OperationalLimitType(){

	}
}//end OperationalLimitType