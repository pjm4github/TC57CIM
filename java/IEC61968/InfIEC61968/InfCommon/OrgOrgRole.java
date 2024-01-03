package IEC61968.InfIEC61968.InfCommon;

import IEC61970.Base.Domain.String;
import IEC61968.Common.OrganisationRole;

/**
 * Roles played between Organisations and other Organisations. This includes role
 * ups for ogranisations, cost centers, profit centers, regulatory reporting, etc.
 * 
 * Note that the parent and child relationship is indicated by the name on each
 * end of the association.
 * @created 29-Dec-2023 6:02:06 PM
 */
public class OrgOrgRole extends OrganisationRole {

	/**
	 * Identifiers of the organisation held by another organisation, such as a
	 * government agency (federal, state, province, city, county), financial
	 * institution (Dun and Bradstreet), etc.
	 */
	public String clientID;

	public OrgOrgRole(){

	}
}//end OrgOrgRole