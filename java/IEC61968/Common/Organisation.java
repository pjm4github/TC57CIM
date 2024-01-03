package IEC61968.Common;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Organisation that might have roles as utility, contractor, supplier,
 * manufacturer, customer, etc.
 * @created 03-Jan-2024 12:12:50 PM
 */
public class Organisation extends IdentifiedObject {

	/**
	 * Electronic address.
	 */
	public ElectronicAddress electronicAddress;
	/**
	 * Phone number.
	 */
	public TelephoneNumber phone1;
	/**
	 * Additional phone number.
	 */
	public TelephoneNumber phone2;
	/**
	 * Postal address, potentially different than 'streetAddress' (e.g., another city).
	 */
	public StreetAddress postalAddress;
	/**
	 * Street address.
	 */
	public StreetAddress streetAddress;
	/**
	 * Parent organisation of this organisation.
	 */
	public ParentOrganization ParentOrganisation;

	public Organisation(){

	}
}//end Organisation