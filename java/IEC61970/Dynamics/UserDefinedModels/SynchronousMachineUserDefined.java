package IEC61970.Dynamics.UserDefinedModels;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics;

/**
 * Synchronous machine whose dynamic behaviour is described by a user-defined
 * model.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class SynchronousMachineUserDefined extends SynchronousMachineDynamics {

	/**
	 * Behaviour is based on proprietary model as opposed to detailed model.
	 * true = user-defined model is proprietary with behaviour mutually understood by
	 * sending and receiving applications and parameters passed as general attributes
	 * false = user-defined model is explicitly defined in terms of control blocks and
	 * their input and output signals.
	 */
	public Boolean proprietary;

	public SynchronousMachineUserDefined(){

	}
}//end SynchronousMachineUserDefined