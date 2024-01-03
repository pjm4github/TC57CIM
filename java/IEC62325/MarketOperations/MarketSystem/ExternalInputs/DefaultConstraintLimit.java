package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Core.Curve;

/**
 * Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit
 * (Y1 and Y2, respectively) applied as a default value if no specific constraint
 * limits are specified for a contingency analysis. Use CurveSchedule XAxisUnits
 * to specify MW or MVA.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class DefaultConstraintLimit extends Curve {

	public SecurityConstraintSum SecurityConstraintSum;

	public DefaultConstraintLimit(){

	}
}//end DefaultConstraintLimit