package IEC61970.Dynamics.UserDefinedModels;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantDynamics;

/**
 * Wind plant function block whose dynamic behaviour is described by <font
 * color="#0f0f0f">a user-defined model.</font>
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindPlantUserDefined extends WindPlantDynamics {

	/**
	 * Behaviour is based on proprietary model as opposed to detailed model.
	 * true = user-defined model is proprietary with behaviour mutually understood by
	 * sending and receiving applications and parameters passed as general attributes
	 * false = user-defined model is explicitly defined in terms of control blocks and
	 * their input and output signals.
	 */
	public Boolean proprietary;
	/**
	 * Parameter of this proprietary user-defined model.
	 */
	public ProprietaryParameterDynamics ProprietaryParameterDynamics;

	public WindPlantUserDefined(){

	}
}//end WindPlantUserDefined