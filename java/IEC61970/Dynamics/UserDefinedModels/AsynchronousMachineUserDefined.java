package IEC61970.Dynamics.UserDefinedModels;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics;

/**
 * Asynchronous machine whose dynamic behaviour is described by a user-defined
 * model.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AsynchronousMachineUserDefined extends AsynchronousMachineDynamics {

	/**
	 * Behaviour is based on proprietary model as opposed to detailed model.
	 * true = user-defined model is proprietary with behaviour mutually understood by
	 * sending and receiving applications and parameters passed as general attributes
	 * false = user-defined model is explicitly defined in terms of control blocks and
	 * their input and output signals.
	 */
	public Boolean proprietary;

	public AsynchronousMachineUserDefined(){

	}
}//end AsynchronousMachineUserDefined