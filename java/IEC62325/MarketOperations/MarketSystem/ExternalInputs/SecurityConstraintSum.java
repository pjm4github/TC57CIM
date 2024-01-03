package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.ReferenceData.RTO;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Typically provided by RTO systems, constraints identified in both base case and
 * critical contingency cases have to be transferred.
 * A constraint has N (>=1) constraint terms. A term is represented by an instance
 * of TerminalConstraintTerm.
 * The constraint expression is:
 * minValue <= c1*x1 + c2*x2 + .... cn*xn + k <= maxValue
 * where:
 * - cn is ConstraintTerm.factor
 * - xn is the flow at the terminal
 * Flow into the associated equipment is positive for the purpose of
 * ConnectivityNode NodeConstraintTerm.
 * 
 * k is SecurityConstraintsLinear.resourceMW.
 * The units of k are assumed to be same as the units of the flows, xn.  The
 * constants, cn, are dimensionless.
 * With these conventions, cn and k are all positive for a typical constraint such
 * as "weighted sum of generation shall be less than limit". Furthermore, cn are
 * all 1.0 for a case such as "interface flow shall be less than limit", assuming
 * the terminals are chosen on the importing side of the interface.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class SecurityConstraintSum extends MarketFactors {

	public RTO RTO;
	public ConstraintTerm ConstraintTerms;

	public SecurityConstraintSum(){

	}
}//end SecurityConstraintSum