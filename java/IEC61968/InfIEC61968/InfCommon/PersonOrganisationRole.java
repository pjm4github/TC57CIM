package IEC61968.InfIEC61968.InfCommon;

import IEC61970.Base.Domain.String;
import IEC61968.Common.OrganisationRole;

/**
 * Role an organisation plays with respect to persons.
 * @created 29-Dec-2023 6:02:18 PM
 */
public class PersonOrganisationRole extends OrganisationRole {

	/**
	 * Identifiers of the person held by an organisation, such as a government agency
	 * (federal, state, province, city, county), financial institutions, etc.
	 */
	public String clientID;

	public PersonOrganisationRole(){

	}
}//end PersonOrganisationRole