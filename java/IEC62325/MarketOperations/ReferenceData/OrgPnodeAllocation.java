package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class models the allocation between asset owners and pricing nodes.
 * @created 28-Dec-2023 12:18:45 PM
 */
public class OrgPnodeAllocation extends IdentifiedObject {

	/**
	 * Maximum MW for the Source/Sink for the Allocation 
	 */
	public ActivePower maxMWAllocation;
	public Pnode Pnode;

	public OrgPnodeAllocation(){

	}
}//end OrgPnodeAllocation