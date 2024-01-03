package IEC61968.InfIEC61968.InfCommon;

import IEC61968.Common.Status;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Enumeration of potential roles that might be played by one object relative to
 * another.
 * @created 29-Dec-2023 6:03:08 PM
 */
public class Role extends IdentifiedObject {

	public Status status;
	/**
	 * Type of role.
	 */
	public String type;

	public Role(){

	}
}//end Role