package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC62325.MarketOperations.MktDomain.RampRateCondition;
import IEC62325.MarketOperations.MktDomain.ConstraintRampType;
import IEC62325.MarketOperations.MktDomain.RampRateType;
import IEC61970.Base.Core.Curve;

/**
 * Ramp rate as a function of resource MW output.
 * @created 28-Dec-2023 5:23:12 PM
 */
public class RampRateCurve extends Curve {

	/**
	 * condition for the ramp rate
	 */
	public RampRateCondition condition;
	/**
	 * The condition that identifies whether a Generating Resource should be
	 * constrained from Ancillary Service provision if its Schedule or Dispatch change
	 * across Trading Hours or Trading Intervals requires more than a specified
	 * fraction of the duration of the Trading Hour or Trading Interval.
	 * 
	 * Valid values are Fast/Slow
	 */
	public ConstraintRampType constraintRampType;
	/**
	 * How ramp rate is applied (e.g. raise or lower, as when applied to a generation
	 * resource)
	 */
	public RampRateType rampRateType;

	public RampRateCurve(){

	}
}//end RampRateCurve