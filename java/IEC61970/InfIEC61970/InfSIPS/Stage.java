package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Stage of a remedial action scheme.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:34:48 PM
 */
public class Stage extends IdentifiedObject {

	/**
	 * The priority of the stage.   0 = don t care (default) 1 = highest priority. 2
	 * is less than 1 and so on. A stage with higher priority needs be activated
	 * before a lower stage can be activated.
	 */
	public Integer priority;
	public StageTrigger StageTrigger;

	public Stage(){

	}
}//end Stage