package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MktDomain.ResultsConstraintType;
import IEC62325.MarketOperations.MktDomain.ConstraintLimitType;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ReferenceData.MktContingency;

/**
 * Provides the Market results for the constraint processing for either the DAM or
 * RTM. The data includes the constraint type (binding or violated), the solved
 * value for the constraint, and the associated shadow price.
 * @created 28-Dec-2023 8:19:36 PM
 */
public class ConstraintResults extends IdentifiedObject {

	/**
	 * Branch base Power Flow.
	 */
	public Float baseFlow;
	/**
	 * This value is determined in DA and RTM. The SCUC optimization ensures that the
	 * MW flow on the Branch Group will not exceed this limit in the relevant
	 * direction. 
	 */
	public Float BGLimit;
	/**
	 * Branch Group TR Reservation Capacity - This value is determined in DA and RTM.
	 * It is the amount of spare transmission capacity that is left for the TR holder
	 * to use. 
	 */
	public Float BGTRResCap;
	/**
	 * MW Limit.
	 */
	public Float bindingLimit;
	/**
	 * Cleared MW.
	 */
	public Float clearedValue;
	/**
	 * Non-competitive path constraint Flag"(Y/N)  indicating whether the shadow price
	 * on a non-competitive path was non-zero.
	 */
	public YesNo competitivePathConstraint;
	/**
	 * Type of constraint.
	 */
	public ResultsConstraintType constraintType;
	/**
	 * Limit flag ('Maximum', 'Minimum').
	 */
	public ConstraintLimitType limitFlag;
	/**
	 * Included in optimization Y/N.
	 */
	public YesNo optimizationFlag;
	/**
	 * Transmission overload MW.
	 */
	public Float overloadMW;
	/**
	 * Actual MW flow as percent of limit.
	 */
	public Float percentMW;
	/**
	 * Shadow Price ($/MW) for the commodity.  Shadow price for the corresponding
	 * constraint.
	 */
	public Float shadowPrice;
	/**
	 * Update time stamp.
	 */
	public DateTime updateTimeStamp;
	/**
	 * MQS change type.
	 */
	public MQSCHGType updateType;
	/**
	 * Updated user.
	 */
	public String updateUser;
	public MktContingency MktContingency;

	public ConstraintResults(){

	}
}//end ConstraintResults