package IEC61968.InfIEC61968.InfCommon;

import IEC61970.Base.Domain.String;
import IEC61968.Common.OrganisationRole;

/**
 * Organisation that is a commercial bank, agency, or other institution that
 * offers a similar service.
 * @created 03-Jan-2024 12:32:45 PM
 */
public class Bank extends OrganisationRole {

	/**
	 * Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is
	 * not yet in operation.
	 */
	public String bic;
	/**
	 * International bank account number defined in ISO 13616; for countries where
	 * IBAN is not in operation, the existing BIC or SWIFT codes may be used instead
	 * (see ISO 9362).
	 */
	public String iban;

	public Bank(){

	}
}//end Bank