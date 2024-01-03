package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.Money;

/**
 * A permit is sometimes needed to provide legal access to land or equipment. For
 * example, local authority permission for road works.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class AccessPermit extends WorkDocument {

	/**
	 * Permit application number that is used by municipality, state, province, etc.
	 */
	public String applicationNumber;
	/**
	 * Date that permit became official.
	 */
	public Date effectiveDate;
	/**
	 * Permit expiration date.
	 */
	public Date expirationDate;
	/**
	 * Total cost of permit.
	 */
	public Money payment;
	/**
	 * Permit identifier.
	 */
	public String permitID;

	public AccessPermit(){

	}
}//end AccessPermit