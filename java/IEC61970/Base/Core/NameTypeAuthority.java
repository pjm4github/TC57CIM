package TC57CIM.IEC61970.Base.Core;

import TC57CIM.IEC61970.Base.Domain.String;

/**
 * Authority responsible for creation and management of names of a given type;
 * typically an organization or an enterprise system.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
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

	public void finalize() throws Throwable {

	}

}