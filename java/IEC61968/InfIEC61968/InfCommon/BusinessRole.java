package IEC61968.InfIEC61968.InfCommon;

import IEC61968.Common.Status;
import IEC61970.Base.Domain.String;
import IEC61968.Common.OrganisationRole;

/**
 * A business role that this organisation plays. A single organisation typically
 * performs many functions, each one described as a role.
 * @created 29-Dec-2023 6:00:57 PM
 */
public class BusinessRole extends OrganisationRole {

	public Status status;
	/**
	 * Classification by utility's corporate standards and practices.
	 */
	public String type;

	public BusinessRole(){

	}
}//end BusinessRole