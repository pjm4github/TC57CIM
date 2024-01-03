package IEC61968.InfIEC61968.InfCommon;

import IEC61968.Common.Status;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Craft of a person or a crew. Examples include overhead electric, underground
 * electric, high pressure gas, etc. This ensures necessary knowledge and skills
 * before being allowed to perform certain types of work.
 * @created 29-Dec-2023 6:01:16 PM
 */
public class Craft extends IdentifiedObject {

	public Status status;
	/**
	 * Classification by utility's work mangement standards and practices.
	 */
	public String type;
	public OldPerson ErpPersons;

	public Craft(){

	}
}//end Craft