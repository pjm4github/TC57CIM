package IEC61970.Base.Core;

import IEC61970.Base.Domain.String;

/**
 * Authority responsible for creation and management of names of a given type;
 * typically an organization or an enterprise system.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class NameTypeAuthority {

	/**
	 * Description of the name type authority.
	 */
	public String description;
	/**
	 * Name of the name type authority.
	 */
	public String name;

	public NameTypeAuthority(){

	}
}//end NameTypeAuthority