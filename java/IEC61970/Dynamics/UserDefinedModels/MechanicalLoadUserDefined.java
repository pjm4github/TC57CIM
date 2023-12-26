package IEC61970.Dynamics.UserDefinedModels;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Dynamics.StandardModels.MechanicalLoadDynamics.MechanicalLoadDynamics;

/**
 * Mechanical load function block whose dynamic behaviour is described by <font
 * color="#0f0f0f">a user-defined model.</font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MechanicalLoadUserDefined extends MechanicalLoadDynamics {

	/**
	 * Behaviour is based on proprietary model as opposed to detailed model.
	 * true = user-defined model is proprietary with behaviour mutually understood by
	 * sending and receiving applications and parameters passed as general attributes
	 * false = user-defined model is explicitly defined in terms of control blocks and
	 * their input and output signals.
	 */
	public Boolean proprietary;

	public MechanicalLoadUserDefined(){

	}
}//end MechanicalLoadUserDefined