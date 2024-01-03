package IEC61968.Common;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Identifies a way in which an organisation may participate in the utility
 * enterprise (e.g., customer, manufacturer, etc).
 * @author T. Kostic
 * @version 1.0
 * @created 03-Jan-2024 12:09:35 PM
 */
public class OrganisationRole extends IdentifiedObject {

	/**
	 * All configuration events created for this organisation role.
	 */
	public ConfigurationEvent ConfigurationEvents;
	/**
	 * Organisation having this role.
	 */
	public Organisation Organisation;

	public OrganisationRole(){

	}
}//end OrganisationRole