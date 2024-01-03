package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Status;

/**
 * Labor code associated with various compatible unit labor items.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CULaborCode extends WorkIdentifiedObject {

	/**
	 * Labor code.
	 */
	public String code;
	public Status status;

	public CULaborCode(){

	}
}//end CULaborCode