package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.ResourceAssnType;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class model the ownership percent and type of ownership between resource
 * and organisation.
 * @created 28-Dec-2023 12:19:05 PM
 */
public class OrgResOwnership extends IdentifiedObject {

	/**
	 * association type for the association between Organisation and Resource:
	 */
	public ResourceAssnType asscType;
	/**
	 * Flag to indicate that the SC representing the Resource is the Master SC.
	 */
	public YesNo masterSchedulingCoordinatorFlag;
	/**
	 * ownership percentage for each resource
	 */
	public PerCent ownershipPercent;

	public OrgResOwnership(){

	}
}//end OrgResOwnership