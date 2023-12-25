package TC57CIM.IEC61970.Base.OperationalLimits;

import TC57CIM.IEC61970.Base.Core.Equipment;
import TC57CIM.IEC61970.Base.Core.IdentifiedObject;
import TC57CIM.IEC61970.Base.Core.ACDCTerminal;

/**
 * A set of limits associated with equipment.  Sets of limits might apply to a
 * specific temperature, or season for example. A set of limits may contain
 * different severities of limit levels that would apply to the same equipment.
 * The set may contain limits of different types such as apparent power and
 * current limits or high and low voltage limits  that are logically applied
 * together as a set.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}