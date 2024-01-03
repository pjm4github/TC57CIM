package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Condition that is triggered either by TriggerCondition of by gate condition
 * within a stage and has remedial action-s.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:35:01 PM
 */
public class StageTrigger extends IdentifiedObject {

	/**
	 * The status of the class set by operation or by signal. Optional field that will
	 * override other status fields.
	 */
	public Boolean armed;
	/**
	 * The default/normal value used when other active signal/values are missing.
	 */
	public Boolean normalArmed;
	/**
	 * Priority of trigger. 0 = don t care (default) 1 = highest priority. 2 is less
	 * than 1 and so on. A trigger with the highest priority will trigger first.
	 */
	public Integer priority;
	public Gate GateArmed;
	public Gate GateComCondition;
	public Gate GateTrigger;

	public StageTrigger(){

	}
}//end StageTrigger