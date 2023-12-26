package IEC62325.Environmental;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A named list of alert types.
 * Note:  the name of the list is reflected in the .name attribute (inherited from
 * IdentifiedObject).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class AlertTypeList extends IdentifiedObject {

	/**
	 * The version of the named list of alert types.
	 */
	public String version;
	/**
	 * The environmental data authority responsible for publishing this list of alert
	 * types.
	 */
	public EnvironmentalDataAuthority EnvironmentalDataAuthority;

	public AlertTypeList(){

	}
}//end AlertTypeList