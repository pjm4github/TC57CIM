package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Core.Curve;
import IEC62325.MarketOperations.ReferenceData.MktContingency;

/**
 * Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit
 * (Y1 and Y2, respectively) assigned to a constraint for a specific contingency.
 * Use CurveSchedule XAxisUnits to specify MW or MVA.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class ContingencyConstraintLimit extends Curve {

	public MktContingency MktContingency;
	public MWLimitSchedule MWLimitSchedules;
	public SecurityConstraintSum SecurityConstraintSum;

	public ContingencyConstraintLimit(){

	}
}//end ContingencyConstraintLimit