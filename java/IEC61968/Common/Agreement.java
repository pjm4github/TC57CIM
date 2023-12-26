package IEC61968.Common;

import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.DateTimeInterval;

/**
 * Formal agreement between two parties defining the terms and conditions for a
 * set of services. The specifics of the services are, in turn, defined via one or
 * more service agreements.
 * @created 25-Dec-2023 8:45:18 PM
 */
public class Agreement extends Document {

	/**
	 * Date this agreement was consummated among associated persons and/or
	 * organisations.
	 */
	public Date signDate;
	/**
	 * Date and time interval this agreement is valid (from going into effect to
	 * termination).
	 */
	public DateTimeInterval validityInterval;

	public Agreement(){

	}
}//end Agreement