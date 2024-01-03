package IEC62325.MarketCommon;

import IEC62325.MarketOperations.MktDomain.ResourceCapacityType;
import IEC61970.Base.Domain.Decimal;
import IEC61970.Base.Domain.UnitSymbol;

/**
 * This class model the various capacities of a resource. A resource may have
 * numbers of capacities related to operating, ancillary services, energy trade
 * and so forth. Capacities may be defined for active power or reactive power.
 * @created 03-Jan-2024 1:56:04 PM
 */
public class ResourceCapacity {

	/**
	 * capacity type
	 * 
	 * The types are but not limited to:
	 * 
	 * Regulation Up
	 * Regulation Dn
	 * Spinning Reserve
	 * Non-Spinning Reserve
	 * FOO capacity
	 * MOO capacity
	 */
	public ResourceCapacityType capacityType;
	/**
	 * default capacity
	 */
	public Decimal defaultCapacity;
	/**
	 * maximum capacity
	 */
	public Decimal maximumCapacity;
	/**
	 * minimum capacity
	 */
	public Decimal minimumCapacity;
	/**
	 * Unit selection for the capacity values.
	 */
	public UnitSymbol unitSymbol;

	public ResourceCapacity(){

	}
}//end ResourceCapacity