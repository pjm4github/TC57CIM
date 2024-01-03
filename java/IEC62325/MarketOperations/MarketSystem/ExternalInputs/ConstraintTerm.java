package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A constraint term is one element of a linear constraint.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class ConstraintTerm extends IdentifiedObject {

	public String factor;
	/**
	 * The function is an enumerated value that can be 'active', 'reactive', or 'VA'
	 * to indicate the type of flow.
	 */
	public String function;

	public ConstraintTerm(){

	}
}//end ConstraintTerm