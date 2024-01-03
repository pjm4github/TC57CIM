package IEC62325.MarketOperations.CongestionRevenueRights;

import IEC62325.MarketOperations.MktDomain.CRRRoleType;
import IEC61968.Common.Status;
import IEC61968.Common.OrganisationRole;

/**
 * Identifies a way in which an organisation may participate with a defined
 * Congestion Revenue Right (CRR).
 * @created 03-Jan-2024 2:02:21 PM
 */
public class CRROrgRole extends OrganisationRole {

	/**
	 * Kind of role the organisation is with regards to the congestion revenue rights.
	 */
	public CRRRoleType kind;
	/**
	 * Status of congestion revenue rights organisation role.
	 */
	public Status status;
	public CongestionRevenueRight CongestionRevenueRight;

	public CRROrgRole(){

	}
}//end CRROrgRole