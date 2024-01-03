package IEC61968.Common;

import IEC61970.Base.Domain.String;

/**
 * General purpose street and postal address information.
 * @created 03-Jan-2024 12:13:34 PM
 */
public class StreetAddress {

	/**
	 * Post office box.
	 */
	public String poBox;
	/**
	 * Postal code for the address.
	 */
	public String postalCode;
	/**
	 * Status of this address.
	 */
	public Status status;
	/**
	 * Street detail.
	 */
	public StreetDetail streetDetail;
	/**
	 * Town detail.
	 */
	public TownDetail townDetail;

	public StreetAddress(){

	}
}//end StreetAddress