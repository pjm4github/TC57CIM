package IEC61970.Dynamics.StandardModels;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Abstract parent class for all Dynamics function blocks.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DynamicsFunctionBlock extends IdentifiedObject {

	/**
	 * Function block used indicator.
	 * true = use of function block is enabled
	 * false = use of function block is disabled.
	 */
	public Boolean enabled;

	public DynamicsFunctionBlock(){

	}
}//end DynamicsFunctionBlock