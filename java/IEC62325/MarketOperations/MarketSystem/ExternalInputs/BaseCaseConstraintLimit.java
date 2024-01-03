package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Core.Curve;

/**
 * Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit
 * (Y1 and Y2, respectively) assigned to a contingency analysis base case. Use
 * CurveSchedule XAxisUnits to specify MW or MVA. To be used only if the
 * BaseCaseConstraintLimit differs from the DefaultConstraintLimit.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class BaseCaseConstraintLimit extends Curve {

	public SecurityConstraintSum SecurityConstraintSum;

	public BaseCaseConstraintLimit(){

	}
}//end BaseCaseConstraintLimit