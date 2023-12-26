package IEC61970.Base.OperationalLimits;

import IEC61970.Base.Core.Equipment;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Base.Core.ACDCTerminal;

/**
 * A set of limits associated with equipment.  Sets of limits might apply to a
 * specific temperature, or season for example. A set of limits may contain
 * different severities of limit levels that would apply to the same equipment.
 * The set may contain limits of different types such as apparent power and
 * current limits or high and low voltage limits  that are logically applied
 * together as a set.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OperationalLimitSet extends IdentifiedObject {

	/**
	 * The equipment to which the limit set applies.
	 */
	public Equipment Equipment;
	public ACDCTerminal Terminal;
	/**
	 * Values of equipment limits.
	 */
	public OperationalLimit OperationalLimitValue;

	public OperationalLimitSet(){

	}
}//end OperationalLimitSet