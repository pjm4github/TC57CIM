package IEC61968.Common;

import IEC61970.Base.Domain.String;

/**
 * Telephone number.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TelephoneNumber {

	/**
	 * (if applicable) Area or region code.
	 */
	public String areaCode;
	/**
	 * City code.
	 */
	public String cityCode;
	/**
	 * Country code.
	 */
	public String countryCode;
	/**
	 * (if applicable) Dial out code, for instance to call outside an enterprise.
	 */
	public String dialOut;
	/**
	 * (if applicable) Extension for this telephone number.
	 */
	public String extension;
	/**
	 * (if applicable) Prefix used when calling an international number.
	 */
	public String internationalPrefix;
	/**
	 * Phone number according to ITU E.164.
	 */
	public String ituPhone;
	/**
	 * Main (local) part of this telephone number.
	 */
	public String localNumber;

	public TelephoneNumber(){

	}
}//end TelephoneNumber