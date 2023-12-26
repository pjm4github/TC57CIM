package IEC61968.Common;

import IEC61970.Base.Domain.String;

/**
 * Town details, in the context of address.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TownDetail {

	/**
	 * Town code.
	 */
	public String code;
	/**
	 * Name of the country.
	 */
	public String country;
	/**
	 * Town name.
	 */
	public String name;
	/**
	 * Town section. For example, it is common for there to be 36 sections per
	 * township.
	 */
	public String section;
	/**
	 * Name of the state or province.
	 */
	public String stateOrProvince;

	public TownDetail(){

	}
}//end TownDetail