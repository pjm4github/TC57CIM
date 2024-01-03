package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketOperations.MktDomain.ResourceCertificationKind;

/**
 * Specifies certification for a resource to participate in a specific markets.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class ResourceCertification {

	/**
	 * market type
	 */
	public MarketType market;
	/**
	 * Status of the qualification ('Y' = Active, 'N' = Inactive)
	 */
	public YesNo qualificationFlag;
	/**
	 * Type of service based on ResourceAncillaryServiceType enumeration
	 */
	public ResourceCertificationKind type;

	public ResourceCertification(){

	}
}//end ResourceCertification