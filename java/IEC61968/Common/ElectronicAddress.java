package IEC61968.Common;

import IEC61970.Base.Domain.String;

/**
 * Electronic address information.
 * @created 03-Jan-2024 12:11:57 PM
 */
public class ElectronicAddress {

	/**
	 * Primary email address.
	 */
	public String email1;
	/**
	 * Alternate email address.
	 */
	public String email2;
	/**
	 * Address on local area network.
	 */
	public String lan;
	/**
	 * MAC (Media Access Control) address.
	 */
	public String mac;
	/**
	 * Password needed to log in.
	 */
	public String password;
	/**
	 * Radio address.
	 */
	public String radio;
	/**
	 * User ID needed to log in, which can be for an individual person, an
	 * organisation, a location, etc.
	 */
	public String userID;
	/**
	 * World wide web address.
	 */
	public String web;

	public ElectronicAddress(){

	}
}//end ElectronicAddress